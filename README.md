# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8eb8dbad-580f-3463-9277-e5d037e25ee7 | -19.6643 | -56.8283 | 2025-12-06 00:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 147.8 |
| 000d2ec5-552d-302c-abff-59a1a6a0a010 | 1.6846 | -50.8452 | 2025-12-06 00:00:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b34ef6dd-8ef3-3ba4-80a2-6473dbed6d75 | -4.4755 | -44.1402 | 2025-12-06 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 89942bb1-41e8-3f0a-b973-436169b6dc50 | -19.6442 | -56.8311 | 2025-12-06 00:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| dcb89ec4-f2f6-3b88-bf54-34d60a23257b | -4.4753 | -44.1632 | 2025-12-06 00:00:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 8f5dac9a-5eac-35a3-8059-119d1df6940a | -20.91315 | -49.24675 | 2025-12-06 00:09:00 | TERRA_M-M | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| 38c7025f-2c5a-3849-8ed7-9ac178696271 | -22.38522 | -43.67691 | 2025-12-06 00:09:00 | TERRA_M-M | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 9b85a701-e6a4-372d-8e90-0283f1fe401e | -20.33604 | -50.19801 | 2025-12-06 00:09:00 | TERRA_M-M | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 95256915-8e92-3aa0-af8e-1c035611dd33 | -22.08463 | -46.82762 | 2025-12-06 00:09:00 | TERRA_M-M | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8e225537-3180-3d6f-b88c-9cf231046c0f | -21.02308 | -48.41199 | 2025-12-06 00:09:00 | TERRA_M-M | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 620e47a4-0ba0-3367-a163-57c29b9a3f4e | -20.91105 | -49.22539 | 2025-12-06 00:09:00 | TERRA_M-M | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| f7c88349-f060-3c29-977b-22036f1748a9 | -20.328 | -50.19375 | 2025-12-06 00:09:00 | TERRA_M-M | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.1 |
| f2bda6cb-1d43-3bb7-bac2-c631a31dea50 | -22.08143 | -46.81947 | 2025-12-06 00:09:00 | TERRA_M-M | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 30676133-1065-380d-9cc4-9ad870c58a6f | -20.32218 | -50.19949 | 2025-12-06 00:09:00 | TERRA_M-M | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 397b13f8-bea4-3742-bf91-8587b24b4060 | -19.6643 | -56.8283 | 2025-12-06 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 158.1 |
| 0d7cf546-804d-3d19-a1e7-a159306bae68 | -19.6639 | -56.8492 | 2025-12-06 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 257fb641-99ca-3c30-95f9-32f6d682518d | -19.6442 | -56.8311 | 2025-12-06 00:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 23ea6c4d-c107-3f9e-8896-3da2275c300d | -2.66425 | -44.99021 | 2025-12-06 00:13:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 73365cc4-4f7e-3762-a245-c9f5066534e4 | -4.07719 | -43.83684 | 2025-12-06 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 56a91449-80fe-3c22-b6ee-f1ff13258872 | -5.18696 | -44.25096 | 2025-12-06 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 650f0849-78b4-35c8-a84a-68a6555c7d21 | -4.37628 | -43.5905 | 2025-12-06 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9ea9b14-9615-3642-9e3e-ae46986d4674 | -2.23233 | -45.59566 | 2025-12-06 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89422e38-b7f5-33b7-a6bb-9a5e8c569180 | -5.18565 | -44.24157 | 2025-12-06 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e6f844e-0e75-36ac-a00d-8139fda6727f | -1.72265 | -45.77671 | 2025-12-06 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9e2d14aa-61af-3a14-838d-ee91c3ebffed | -2.02291 | -46.27373 | 2025-12-06 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c39d6da6-f891-3a88-b8f0-d65d1b5b7e09 | -4.07576 | -43.82685 | 2025-12-06 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ab7287e0-6d14-33ce-acc4-a317c3fbf468 | -3.13743 | -44.3586 | 2025-12-06 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 3bfd924c-b283-351d-84d4-ffa2ab0b224f | -2.17023 | -47.88075 | 2025-12-06 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3e96203a-2508-32c1-8b27-a781a084f4df | -0.96126 | -47.32685 | 2025-12-06 00:13:00 | TERRA_M-M | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f99e7775-73c0-383a-83f7-3c48d51d8fa3 | -2.61279 | -47.01375 | 2025-12-06 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd14f7b9-75bd-3af6-b657-b13b10e761e5 | -3.31786 | -44.06178 | 2025-12-06 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0ba7249f-eace-3835-b4eb-9b0563edcc7a | -4.33388 | -43.83245 | 2025-12-06 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 43697aa7-1962-3038-86f4-5d1ce3e121f0 | -1.62221 | -54.72271 | 2025-12-06 00:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 0c683aa8-ba87-3f59-a497-079603248063 | -5.57778 | -43.75379 | 2025-12-06 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a629243a-1703-3e40-a438-326be25b001d | -2.66295 | -44.98101 | 2025-12-06 00:13:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ec9fc42a-d40c-3dd3-bd34-4f8a3715f68e | -3.66846 | -43.55623 | 2025-12-06 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 238b7e2b-d66a-3c27-b52a-05dea1208441 | -2.4343 | -47.18732 | 2025-12-06 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 205d653a-ad14-335c-96a7-b1782a66db05 | -3.8767 | -41.58578 | 2025-12-06 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 4d648ef7-8934-353b-b419-041af232cf39 | -5.139 | -38.03437 | 2025-12-06 00:13:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 33.3 |
| d7e75a26-cec3-3a2d-9341-e9f7f66fa6aa | -2.54967 | -46.01999 | 2025-12-06 00:13:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 232e71e5-9a91-3589-970b-b118005e20b1 | -5.2765 | -43.64544 | 2025-12-06 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 863fc9be-aa71-3609-8913-1f9731872dc9 | -2.20755 | -46.14624 | 2025-12-06 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4c1bbc06-5906-3b1c-8d70-3159dfeb9150 | -1.86171 | -45.58105 | 2025-12-06 00:13:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aa365b0-8a92-3a79-90b8-fe998d12a9f3 | -1.4846 | -45.58527 | 2025-12-06 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2a977917-7842-3d79-b726-5d1c79b3f27e | -4.33531 | -43.84238 | 2025-12-06 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c0a5eb36-e45d-385b-97d6-411d8b51e2bd | -1.70355 | -46.36979 | 2025-12-06 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26bfcaac-3c07-3790-ab6f-a319dff99abd | -4.32856 | -43.83911 | 2025-12-06 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 289d4b37-cab0-3bc5-b7f3-f385c613efa4 | -2.65393 | -44.98228 | 2025-12-06 00:13:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ecc6d001-81d4-3d43-8795-ee7e0f96592f | -1.80978 | -45.7401 | 2025-12-06 00:13:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 50be8de4-5319-3b10-806e-bee4f9fc6f4e | -2.02417 | -46.49451 | 2025-12-06 00:13:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f9899c8e-ef58-3041-9396-73961c1f8ec1 | -3.48035 | -43.39107 | 2025-12-06 00:13:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7a2516a0-7766-33c3-89b9-781d694b2343 | -2.16895 | -47.87142 | 2025-12-06 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a51e7234-bcdd-38f8-aebd-cd2b134bc574 | -2.20634 | -46.13745 | 2025-12-06 00:13:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d400be3d-b69f-30c0-8e21-d957b4ad432f | -2.59319 | -46.87169 | 2025-12-06 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea80e86a-a032-36c5-b0fc-c54feadb4dff | -2.97847 | -47.93456 | 2025-12-06 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 82334462-801a-3573-b5b9-6481167fd313 | -1.69473 | -46.37103 | 2025-12-06 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ffd2620e-7219-359c-bbd7-b17ca24170b7 | -1.17404 | -46.13411 | 2025-12-06 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 21c6d31c-6357-367b-8941-76fd94654eac | -2.80557 | -47.34085 | 2025-12-06 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 05e3ca20-373d-3860-980c-c841e8c2c0a2 | -4.53811 | -44.2228 | 2025-12-06 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b4eeeec5-7e56-36ef-ae8d-e8c124420e69 | -4.38574 | -43.58908 | 2025-12-06 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cf02dfee-866e-3b8b-bcc4-fc1aed2a6f6d | -1.85951 | -47.30089 | 2025-12-06 00:13:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b01d9489-3a2d-32cd-b9e2-8aa1d084b148 | -2.79661 | -47.34208 | 2025-12-06 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7814cf4b-8f31-3592-9e18-33a4a2039fc1 | -2.30864 | -46.08123 | 2025-12-06 00:13:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9c9ecf97-7ac9-3c98-903b-ebe8595eeff3 | -4.32717 | -43.82916 | 2025-12-06 00:13:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9da844ce-a896-3043-8fde-b8300b06984f | -2.08142 | -46.16119 | 2025-12-06 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| afb1256b-cefb-3259-8c19-6aa8aa5a7ef0 | -2.79785 | -47.35115 | 2025-12-06 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 515e3477-a4d3-39db-a79b-df4bdea145a0 | -4.16427 | -39.24799 | 2025-12-06 00:13:00 | TERRA_M-M | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 18.0 |
| e9d23bad-3f52-3e27-8fe3-f08a073e85b8 | -3.13607 | -44.34898 | 2025-12-06 00:13:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 17b485f7-df68-3a02-8478-b0394cf9d590 | -2.24042 | -46.12371 | 2025-12-06 00:13:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cfe146c0-23b6-343f-9e04-0acc7744b78e | -2.43554 | -47.1963 | 2025-12-06 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 781259b3-7b40-3244-8313-c62553451dbc | -2.16116 | -47.88203 | 2025-12-06 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3ea303ce-12f8-35e5-9b20-58f5516d7514 | -1.62167 | -54.71753 | 2025-12-06 00:13:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| a824d3cb-0c1a-3cac-a1ed-cce605fa2d70 | -2.41 | -46.4724 | 2025-12-06 00:13:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4fb660ea-cbc9-3d28-972f-351a083a3368 | -2.97718 | -47.92503 | 2025-12-06 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5996f4ac-c1cc-3414-a63a-eee35388e4f3 | -2.65523 | -44.99149 | 2025-12-06 00:13:00 | TERRA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 51332d0b-2cbd-3e1d-a68c-d78a074bd7a4 | -4.53678 | -44.21331 | 2025-12-06 00:13:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8884f41e-a0a4-340a-99a2-4001e664ff01 | -1.86295 | -45.59002 | 2025-12-06 00:13:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 45dc6c90-d609-3b9f-803d-401947eec9f5 | -2.03113 | -46.60981 | 2025-12-06 00:13:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| be67e41b-2ee8-3a77-b37e-b40868133681 | 3.41284 | -51.27885 | 2025-12-06 00:15:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a258ed84-4497-32ec-9698-0380dd7fee17 | 3.41462 | -51.26655 | 2025-12-06 00:15:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e8b06b74-ab82-3ae0-8b19-c2dc7a2bf98a | 2.90951 | -51.00872 | 2025-12-06 00:15:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 752270f9-d7c0-3bde-b8f8-2dfa60808d8d | 1.69564 | -50.84952 | 2025-12-06 00:15:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3b8d3ac1-1261-3438-b064-86346f20a949 | 1.68704 | -50.83586 | 2025-12-06 00:15:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 0564fa5d-480d-30eb-8649-24069221636f | 1.69414 | -50.84268 | 2025-12-06 00:15:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f0e65318-0979-3f0a-9b1d-ce1600789108 | 1.68535 | -50.84805 | 2025-12-06 00:15:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2fd51a99-1a37-3949-aada-2a48792b6158 | 3.65874 | -51.28889 | 2025-12-06 00:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 72b802a4-5328-3272-b604-08f94116ed3e | 3.50742 | -51.2607 | 2025-12-06 00:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a1573705-5004-3fe7-a92a-da68f071e8ed | 3.45937 | -51.24797 | 2025-12-06 00:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4b9ae9fa-b820-35d6-aae9-cb4f21852d1e | 3.65718 | -51.28187 | 2025-12-06 00:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 74cf404c-b62f-3177-a1f4-a8b260ccae19 | -19.6643 | -56.8283 | 2025-12-06 00:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 152.3 |
| 7e94d0ad-82d5-3ed0-82d3-ef02a862092a | -2.4585 | -45.3641 | 2025-12-06 00:20:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 13e0a6dc-e2fc-38a9-b711-26e8cc67a7a6 | -19.6643 | -56.8283 | 2025-12-06 00:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 160.0 |
| 8706f5c9-e1e6-314f-8c88-fc0d4c544693 | -19.6643 | -56.8283 | 2025-12-06 00:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 145.4 |
| e6447aba-506b-399b-b287-c8e4d4eb3d30 | 1.6921 | -50.8335 | 2025-12-06 00:40:00 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b00e519c-b21d-3de8-9109-dd33184d77af | 1.9975 | -55.674599 | 2025-12-06 00:40:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 427b7405-ef32-3ec2-bd23-9407193242cf | 1.6955 | -50.818699 | 2025-12-06 00:40:00 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 92c46c26-c291-30db-85e4-31af10ab2c87 | -19.6643 | -56.8283 | 2025-12-06 00:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 6dc529a9-f1cb-362a-a363-ea1ec5d15dd4 | -19.6442 | -56.8311 | 2025-12-06 01:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 0ade5531-9043-3194-bc6c-a07fdcac53bc | -19.6643 | -56.8283 | 2025-12-06 01:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 193.1 |
| 07ba7456-fbc3-34fc-bf30-f654f6a96b80 | -19.6844 | -56.8254 | 2025-12-06 01:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |


[Clique aqui para ver as próximas entradas](README2.md)

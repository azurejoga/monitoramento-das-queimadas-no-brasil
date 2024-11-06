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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6855d924-5f85-3c07-9b30-02aad157d9b9 | -6.49548 | -47.48177 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0c0b32c2-643a-37cc-bd40-18e8be671de2 | -6.12589 | -43.98656 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4e07a29c-2316-33b6-8ba0-3c19d5463fac | -5.93624 | -43.77817 | 2024-11-06 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e5df084e-7c88-3bbb-a29c-f4fc3a0ff1f9 | -3.1437 | -49.13697 | 2024-11-06 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba6d6e4a-36cb-3132-9282-88c7f4ef2d44 | -6.60945 | -41.64964 | 2024-11-06 03:49:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c3909d6-d1a3-31e7-af53-34a68a0e78dd | -6.05461 | -39.43386 | 2024-11-06 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 175b868c-15cd-3901-b0ee-8046485ee0ec | -5.06859 | -44.23045 | 2024-11-06 03:49:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 285d205f-dd50-3b6e-84a8-01cd303e5ec2 | -9.47609 | -40.37687 | 2024-11-06 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 40b3b59a-c3a0-3e11-830d-01007be83ac1 | -6.95482 | -47.86076 | 2024-11-06 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5d7b7f7-9702-3649-8768-22856d1052e8 | -6.6213 | -41.65155 | 2024-11-06 03:49:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 62b853b2-ce66-36a2-abdd-e52f0fa3614c | -5.98325 | -45.36461 | 2024-11-06 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82bcd0a5-6291-37ec-a68b-5f677918929d | -5.97811 | -45.36379 | 2024-11-06 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13b24939-2767-3711-85d8-8f7bdbc1f893 | -11.73009 | -37.6136 | 2024-11-06 03:49:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cb270edb-9523-3408-9e50-a6b0a98aa571 | -4.73438 | -43.24931 | 2024-11-06 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97f3531b-7ae2-355c-8831-bbb14cc68b62 | -5.8903 | -39.23649 | 2024-11-06 03:49:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc848017-d9d0-3f67-98b4-a9a5e6f73dbe | -6.13141 | -43.98238 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2427d883-13d9-3f97-b172-9a2f554f24a5 | -7.37742 | -43.50712 | 2024-11-06 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcea1f71-01f7-31be-bdf8-41fc413a0aeb | -5.62754 | -44.18393 | 2024-11-06 03:49:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20fbeff3-7e4d-3bae-90eb-a720a3bf4dbf | -3.55013 | -47.39273 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8b143b8-d4ce-3dce-ab04-11091e13eaa4 | -3.75431 | -47.60023 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0899412-a9b0-3cc6-9551-9b6db7e5a320 | -6.05045 | -39.43727 | 2024-11-06 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 399373ac-2c46-340a-a09b-32efd0c22252 | -8.76577 | -40.34907 | 2024-11-06 03:49:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 795b18bc-4465-3b90-8ae1-55f3d3be7324 | -6.13443 | -43.97413 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a1b5aab9-c1c2-318a-806c-3339364035cf | -7.59437 | -35.11809 | 2024-11-06 03:49:00 | NOAA-21 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da23ea1d-7adb-317b-bffe-9d07eb69eec9 | -9.53296 | -40.34063 | 2024-11-06 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 153b3b92-debd-3261-bace-738adae97d80 | -6.95179 | -47.86317 | 2024-11-06 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc86408d-9e60-3c96-94b4-d2e008dcf75f | -3.53876 | -47.38601 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7ddc6065-86eb-3308-9d92-c0bc037b0236 | -7.52537 | -40.1471 | 2024-11-06 03:49:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2eead76c-5105-3db8-a247-ba11e3d71d37 | -6.13524 | -43.96926 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5022f8fa-a617-3428-bdd6-d8b02980704e | -4.55891 | -48.00956 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f9e02e73-174e-33fd-8caf-f03b212125bc | -6.12979 | -43.97333 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 59c34f3d-cd45-34f9-a08d-4df18f826713 | -2.84499 | -49.46808 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 62411fa5-7efb-31dc-9c54-9dbd398974b7 | -5.63775 | -46.68067 | 2024-11-06 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d02b867-1c2f-359e-b459-28014aa21a08 | -3.97197 | -48.16854 | 2024-11-06 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ea67e201-3d7a-3c4a-9496-ca4654f47375 | -4.3353 | -39.36281 | 2024-11-06 03:49:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 84991306-110d-3307-880a-5f5448b336f4 | -4.55801 | -48.01455 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1c25b129-7a0b-3646-85e7-49e4a5befbb5 | -6.36897 | -47.9237 | 2024-11-06 03:49:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 092b1463-d114-3a3f-8dfd-7c473e5af013 | -6.13361 | -43.97906 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ccf2313f-da91-3f6c-b64e-1ababdfb10c5 | -4.13348 | -43.57837 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 640d726b-0b7d-3954-80e8-ec9f59f30c93 | -5.50526 | -47.16689 | 2024-11-06 03:49:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b833de7-84e6-3448-91e7-6d8b037c21e2 | -4.63248 | -42.81231 | 2024-11-06 03:49:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8278c793-df63-3712-8028-ec37fc11d092 | -5.5523 | -43.70569 | 2024-11-06 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e330eaba-9aae-3413-833e-758a849aaac9 | -3.99814 | -43.25214 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7774c106-d85e-326c-9c1a-8dc737d8012c | -3.79838 | -44.03311 | 2024-11-06 03:49:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acca56a5-dc31-3fe3-88a1-cb7336517bb5 | -4.29479 | -46.35071 | 2024-11-06 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5785f0c-fa13-3028-9185-f9f5c8fe71e2 | -7.19968 | -43.14328 | 2024-11-06 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e4a8dc1-e123-38d8-b5a2-ce45ab71fed7 | -6.77 | -37.53498 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf882eef-e160-3210-a9c3-a95ab88ffad6 | -9.62574 | -35.86898 | 2024-11-06 03:49:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 49a5306f-428e-3443-abc5-7c16ecdaf1e2 | -6.85067 | -38.89791 | 2024-11-06 03:49:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 77153c04-4548-300f-bcba-c01b10690424 | -11.08991 | -37.37843 | 2024-11-06 03:49:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42d32f33-7f18-3d3f-beb8-0e9dbdfeabc8 | -6.53586 | -39.73318 | 2024-11-06 03:49:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a4bb8ad9-f666-378d-b8e3-87c031b95e8a | -4.74548 | -38.46679 | 2024-11-06 03:49:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7be3f9c7-b148-3ca7-a006-5ca9080944b0 | -4.5503 | -38.39064 | 2024-11-06 03:49:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f33fca46-40e0-343f-9e9a-cea0176ebf2b | -10.52509 | -42.39612 | 2024-11-06 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 78bf8b1c-75ca-34e9-9821-f5953375e258 | -5.65909 | -45.93378 | 2024-11-06 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ed8531d-6240-30e0-89aa-f7ce2ed5b433 | -3.55257 | -47.37845 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0a30ea-86c5-3870-9c2a-49bc3dd6ecd7 | -11.26576 | -41.03962 | 2024-11-06 03:49:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2ada51ea-be09-3dd6-bde3-1bda20aeced1 | -9.53362 | -40.33661 | 2024-11-06 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aaf5ab25-7b1c-32a4-bc47-852b99ab6c03 | -5.14375 | -47.70338 | 2024-11-06 03:49:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61031362-8f2a-3451-98e4-ef732a06eb80 | -7.83483 | -35.03393 | 2024-11-06 03:49:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cd94ddfc-23d3-36b8-b176-297bea94778b | -2.84539 | -49.47132 | 2024-11-06 03:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 9ab346f0-7a7d-3ef2-b489-d951dbe58793 | -9.89203 | -42.08849 | 2024-11-06 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 87c6c6b9-f50b-392f-815c-ef5ac2fbf230 | -11.26866 | -41.04436 | 2024-11-06 03:49:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8bf5749-8a15-3aca-b0b5-5d6294225ce4 | -7.0176 | -39.28388 | 2024-11-06 03:49:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb18891d-b495-3a02-97d7-aa2746aeff5d | -7.46633 | -35.08327 | 2024-11-06 03:49:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 15067e8e-a820-3463-a1cd-3a9ddc47f676 | -3.75837 | -45.93677 | 2024-11-06 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecefad69-15a6-3aad-9480-45b637b28184 | -5.5569 | -43.7065 | 2024-11-06 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a8b1f35b-0985-3fdf-a022-04caf3225498 | -7.5496 | -42.84832 | 2024-11-06 03:49:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f54ccc91-e8cc-3db4-9eec-09afd9490cd5 | -6.36297 | -47.92257 | 2024-11-06 03:49:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10a076c8-ce1a-3753-86cd-ef6d8e80ed38 | -7.67189 | -42.64493 | 2024-11-06 03:49:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 447a284b-8a66-3e27-ac74-eb0ad8c8d2cb | -6.49673 | -44.68578 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 65e2b04c-a843-3996-9113-3b29ace201eb | -4.77263 | -48.67908 | 2024-11-06 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 11e7ad7d-21e6-3eb7-9d50-b69ce8c008f5 | -9.89286 | -42.08356 | 2024-11-06 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| af3ce2f7-6dbc-39b8-a5ea-499d628fae4e | -4.3544 | -46.52979 | 2024-11-06 03:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f6877c36-00f6-35e8-ace6-28cae7b9ce39 | -7.01582 | -39.99311 | 2024-11-06 03:49:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8d1d13f8-1376-3925-8b37-6a253f65264a | -8.50339 | -42.10414 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1ec31688-b023-3645-af36-fd7ac43a3111 | -6.12502 | -43.99152 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ac950ee-fe5f-30c5-88f4-9edcfced1163 | -6.30154 | -35.22549 | 2024-11-06 03:49:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 52bf6d42-40d9-3455-820c-053ff99a53da | -3.53707 | -47.39585 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e7bab75-5658-36af-8a66-62cbbeed305a | -4.58941 | -45.49601 | 2024-11-06 03:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06f4884c-3ba5-3d95-bf0f-4c807b9b5dcf | -5.3248 | -43.07619 | 2024-11-06 03:49:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| db8937c9-630f-3d35-ad86-418d9274825b | -6.5132 | -44.6771 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7f06b334-c04a-373b-ab85-4283ce30041b | -6.50087 | -47.49047 | 2024-11-06 03:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 07331188-2743-3a9e-97ec-06bf3fd004a7 | -3.54105 | -47.3727 | 2024-11-06 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e44d9d16-86dd-3187-932a-c7786699fb76 | -5.98734 | -45.37154 | 2024-11-06 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0f466c79-822a-3d06-8039-c0268c151153 | -5.14229 | -35.88766 | 2024-11-06 03:49:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 68ffb8f0-b2da-3133-a2ab-cbb0297f276e | -5.15415 | -43.77849 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391688df-83fb-3474-ae2f-9c1f5cf963c4 | -4.12798 | -43.58263 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c1eb55e6-acb8-3e8f-bc5d-d8ae77e8224c | -4.83459 | -42.79358 | 2024-11-06 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 655cb277-920a-33d4-b474-8b77dda14a2c | -5.23136 | -48.13734 | 2024-11-06 03:49:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06ae2a28-571e-3fbf-bfad-02a70268b680 | -4.13611 | -43.57746 | 2024-11-06 03:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 469f2ec1-f65a-3141-a398-cf12e9e0da14 | -6.51226 | -44.6826 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fca82876-8e8b-3080-8adb-e180dddc5b8f | -6.4919 | -44.68477 | 2024-11-06 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ff23c838-6c68-30d1-adc5-c7aa667e800c | -4.73716 | -43.25182 | 2024-11-06 03:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb3b0874-e1bd-3e73-b11b-328b25f30630 | -5.55392 | -43.69624 | 2024-11-06 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e173f80d-c00a-3496-b943-e29bea597fa9 | -8.50425 | -42.09894 | 2024-11-06 03:49:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ec3d3539-cf8b-303b-b97f-f00f18cc7b72 | -5.63841 | -46.67686 | 2024-11-06 03:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfcf8d31-712f-3e7f-aee4-5950cbecee35 | -5.22568 | -37.38008 | 2024-11-06 03:49:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e0a28d0b-649a-39bb-a724-6beca2b6652e | -6.10733 | -43.96465 | 2024-11-06 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1dea9eb3-fef5-37cf-9e7e-95d346f77fac | -6.43162 | -43.77531 | 2024-11-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)

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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bc4f6ec-0f3b-3e65-a97d-bad7b4bb6ec4 | -3.37856 | -50.44053 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9b137db-efe3-3306-b099-f472a8b17759 | -6.29025 | -41.78452 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| beaa1388-cb13-37a4-ad79-0cf2983c7c23 | -7.10628 | -43.575 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e701946-8c87-3598-8d18-0a787f9008bb | -7.34637 | -44.64465 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db49cdde-ec08-329a-be6b-73e36c1122c8 | -2.81388 | -50.46708 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 578a69f8-528c-3abe-80ce-b04c903b6c4a | -3.57392 | -43.46578 | 2026-09-18 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af6a33a0-1565-3e92-b0c8-e4707b34f57b | -7.9357 | -44.83307 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85a86186-4e37-35a7-b2ec-08382440a797 | -7.68384 | -46.09324 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 84f74727-5db4-329f-8ebe-12301cb8bc19 | -2.83453 | -48.65087 | 2026-09-18 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87b3b09d-1d76-336d-9439-c89331587f58 | -7.53568 | -46.64389 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54d847f6-7fd4-3728-aa73-e0ee3e4653c2 | -7.47946 | -45.29637 | 2026-09-18 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 059aecbc-a10f-3b85-9d5c-36ccf50c75f8 | -7.1481 | -44.5635 | 2026-09-18 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08ed7123-caa0-3833-be73-93ba87263101 | -7.14611 | -42.08832 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf8b8f3f-2f37-3bf9-a779-53465ea30df3 | -6.45342 | -52.84837 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfac2425-dac5-38a6-acc1-674474b4fd44 | -2.36102 | -55.23466 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a086112-b952-365d-ac92-c924c159f787 | -7.94556 | -44.81323 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5629c11-1f3d-327f-a525-4d33258ea9e5 | -6.41277 | -43.4698 | 2026-09-18 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b0598c71-d81a-3d95-b3df-93307564ed36 | -0.78127 | -47.55072 | 2026-09-18 04:19:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed109a05-bf80-39dc-8cd9-ab88d12eaa43 | -7.63875 | -46.162 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81d7b6d7-e738-3818-8e19-977f3a5f0a12 | -7.14578 | -42.16283 | 2026-09-18 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da537f05-4aaf-3eb4-83f5-3de0514e92ae | -2.90238 | -54.18081 | 2026-09-18 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f95d3ab-3214-3279-831d-dc6ec683d81b | -6.01221 | -51.77198 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31ff1a40-0833-3b85-add8-6dcbac267546 | -6.77816 | -39.27978 | 2026-09-18 04:19:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6811ebff-c27f-3092-94a7-b39a624dfe48 | -1.788 | -47.83738 | 2026-09-18 04:19:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0ec8f8bd-ca37-3a71-85bc-23ff9cce5387 | -4.56745 | -42.9531 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2823d10e-15c2-3a8a-b001-a0264a53fc66 | -4.88665 | -56.06475 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce8cecf1-70bc-3bdd-b97c-e4259edf4c16 | -5.73944 | -52.2481 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73058190-10a4-3162-b28a-1d023be9c393 | -7.86358 | -44.83955 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73dc5266-3905-3cc2-99ee-7b42dacb20b1 | -7.66241 | -45.84173 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aee64872-b01b-3e58-95ab-728a35166d6c | -1.16028 | -47.63417 | 2026-09-18 04:19:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c189c1d7-1b05-32f9-9cb8-688ca2b63a74 | -7.04626 | -42.07811 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0d9e9c37-e989-3e19-a323-5ec63fca9093 | -3.36912 | -50.44337 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3eebce25-248b-3670-9914-8f7eae63f253 | -5.62436 | -40.86475 | 2026-09-18 04:19:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7161820d-d7f2-345f-b167-3cc87dc06903 | -5.58404 | -48.10418 | 2026-09-18 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6beef937-edfc-3725-aeab-3293ddbef521 | -7.04749 | -42.07001 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f05a021-2d70-3735-ba35-59987ceba5a8 | -1.18951 | -48.8078 | 2026-09-18 04:19:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 582bd710-0c93-3317-bdbf-6a0c19c12ae8 | -2.37052 | -48.42923 | 2026-09-18 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebaa7fce-c0b0-3c7c-91ed-ef512ff0054b | -4.56015 | -42.95566 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1ea3b88-1142-3456-becc-e574c06838e0 | -2.49507 | -49.41591 | 2026-09-18 04:19:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03f872d2-6a73-3c05-9fac-76c867b3af37 | -3.99733 | -48.39368 | 2026-09-18 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f4d3c7a-a162-3690-8897-4b3a78d27abf | -7.66664 | -46.09413 | 2026-09-18 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 621a41ca-287d-38a1-b0f5-26857f213c67 | -2.83084 | -50.47421 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3cfb4948-7a2f-3c55-8e38-77537eba4bfa | -3.4861 | -54.72417 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a64c4f64-509d-378d-8a0f-c146d694d709 | -6.88886 | -45.52593 | 2026-09-18 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1848d9cd-694b-30a9-b5a6-74c2be216a87 | -6.29261 | -41.79329 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 51037e3a-e563-3b08-b405-ce1be2f915c6 | -5.75313 | -45.08989 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eddd88ef-d0e8-3ba0-9851-ebf123458347 | -7.03104 | -42.03384 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d703818f-9aaf-3f73-9742-fd2fe0d8b44e | -4.27493 | -55.55165 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ef747e5-b163-31c7-bdea-464358986e4a | -7.02624 | -42.04146 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9e6af3e4-8466-3659-a6c9-db6af518b71b | -4.42985 | -55.52787 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 814f7a88-83e6-3dcf-88bd-72638157fa44 | -7.82264 | -44.90408 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 769c44b6-0032-3c3f-b557-5b73e23aa97b | -6.67206 | -43.63748 | 2026-09-18 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4e5921c-9630-3d6b-a51b-d3d6c8684f1a | -4.55286 | -42.95823 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b7aa57a-1043-3a2b-b9fd-72d61f302871 | -2.82425 | -50.48671 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 100ea9ae-c597-372a-b306-f7a6f349d768 | -4.40676 | -44.38661 | 2026-09-18 04:19:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a62e3df-0345-3f4f-ad6a-d35f16790c3c | -6.27122 | -51.74716 | 2026-09-18 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 000f3e95-248b-3dee-bdfc-77f993217141 | -7.02028 | -43.62855 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3615d0de-e6e5-3a87-92cf-5817f48c34eb | -7.8072 | -44.89456 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e49c63f8-3e3b-34d6-afee-214706462ccf | -2.82642 | -50.4735 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 83431ef6-d064-3b20-adff-236c585a6463 | -6.35196 | -44.08257 | 2026-09-18 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c542688e-8c27-3c3a-8c83-bf9bdaab6d96 | -2.96786 | -52.14155 | 2026-09-18 04:19:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 208a86e5-65d4-370a-83ff-01ccea21e944 | -3.4735 | -54.69221 | 2026-09-18 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2db99e14-82eb-3c89-9909-5bc2eed08c33 | -7.013 | -43.63109 | 2026-09-18 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4789e5db-4b98-3456-b364-ce7a9cd532f3 | -7.79459 | -44.91032 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ee5cd396-5f03-30e1-bff5-398edab8fbaa | -7.07913 | -41.76205 | 2026-09-18 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 16806e45-0253-3021-bc4c-da3743eed761 | -6.44481 | -44.95186 | 2026-09-18 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2097f900-d2e3-37dd-92f8-182cb5dfe602 | -7.34298 | -44.62276 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac2bc08e-6a19-3e31-bfe4-d4d21f87768a | -7.86573 | -45.15207 | 2026-09-18 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc7a664a-89b5-390d-9a59-9cfb05c2d51e | -7.83248 | -44.88433 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 209271fd-1cbf-35b6-b66a-23c107bf0d70 | -7.4597 | -46.83738 | 2026-09-18 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8955b663-7690-38db-8c7d-e2db2f5ddf65 | -5.87876 | -44.6327 | 2026-09-18 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db8cda2a-1e64-3582-a23f-e3e018d21dfd | -7.29527 | -38.96366 | 2026-09-18 04:19:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d92db78-5d17-3f4b-87cf-7f1f76e767ed | -7.07976 | -41.7578 | 2026-09-18 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ff5ec048-7a7e-34d8-8b3a-424a43743f9e | -2.86983 | -49.62546 | 2026-09-18 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6dce6b3d-f2a7-34e0-9ded-1cc39ef12902 | -7.05891 | -47.47389 | 2026-09-18 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d20323e5-bc05-339e-a38a-82d326571eee | -6.93424 | -43.11639 | 2026-09-18 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a99876ab-1de1-3ca8-85c5-34e48c97ead1 | -4.58376 | -42.95929 | 2026-09-18 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 76126425-e5cc-39ed-afcb-7601e62363ad | -2.96215 | -50.33555 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b2bc6ed-e258-3efe-9651-58f809513fcd | -6.65436 | -50.91924 | 2026-09-18 04:19:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a5262bb-a547-3c2d-b8e2-fddb124dc630 | -7.80666 | -44.89802 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5fe7cf7-32a6-3e75-9ed1-79b8112cb5cb | -2.80973 | -50.46788 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76f37aac-935f-37b9-9113-7089a8cd4b41 | -3.26887 | -54.26774 | 2026-09-18 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26d21d5a-a340-3d65-b750-52ec603628aa | -4.23737 | -40.63048 | 2026-09-18 04:19:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9bf60deb-8d11-3693-988b-4dfa6c096e97 | -4.47632 | -54.97283 | 2026-09-18 04:19:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed0b8688-e7b5-3119-8b4d-8482f485349c | -7.34798 | -44.63426 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06e4cd8c-3ace-31c8-adc3-168fb2334be1 | -7.79844 | -44.90738 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47b8ab7b-2fce-3dee-acfc-ad312b3d4200 | -7.80752 | -44.82716 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfd324f8-b3a2-368f-a630-3649e660d189 | -6.32313 | -41.78542 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 75cb5e84-8b9d-3fdc-beda-2be2f7f787a1 | -7.79176 | -44.88505 | 2026-09-18 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d8e1638-6cc6-36d6-817b-3fc25fcf3e93 | -7.81005 | -45.11852 | 2026-09-18 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 004b77d9-ee4b-34ba-be3b-f76b638a9e78 | -5.58039 | -48.10357 | 2026-09-18 04:19:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbe361e4-1b8e-3025-939d-2af7c20036ce | -6.30285 | -41.7739 | 2026-09-18 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 026a034b-3a04-3ba1-ae47-2dd0c874accd | -4.77727 | -55.71257 | 2026-09-18 04:19:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e39509c-be6a-30b3-8dfd-c33f58c9c256 | -7.03854 | -42.081 | 2026-09-18 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e82a60f9-924a-33c7-9702-d9cae95650f8 | -5.7708 | -45.10679 | 2026-09-18 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3debb421-3fa5-3832-b771-8faa4c911c33 | -2.83012 | -50.47859 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ed73f7a4-0e79-3bc9-8aca-ac533d3d93b7 | -6.91127 | -41.71342 | 2026-09-18 04:19:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| baa2dca6-ad7d-3b79-b736-6cc9f0d4792b | -0.78151 | -47.55335 | 2026-09-18 04:19:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4c04ef7-71f5-3077-811e-3e4e62b0de0d | -6.61503 | -44.20597 | 2026-09-18 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bec34242-c266-3d05-a583-09ee2c149767 | -2.8294 | -50.483 | 2026-09-18 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |


[Clique aqui para ver as próximas entradas](README36.md)

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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 813980f7-760f-31bc-b3fe-d64be37354bb | -3.07611 | -50.56858 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1342c532-b3f7-3965-8658-b2bb747b84ec | -5.12685 | -55.95426 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b9268ec-fa9a-3d5a-b6d5-e524f073311d | -1.22537 | -54.14188 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b309c7b1-433b-3366-91dd-9eb0d2abb08e | -7.25125 | -46.16401 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 811684ec-d6f5-3522-8562-83b9c5cdf35d | -7.46104 | -46.14733 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c68796ed-46c0-34b9-a557-75f0b342f549 | -2.89584 | -50.42051 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e801ae8-10c1-3cb4-abe3-d02c116a5875 | -3.41821 | -58.21221 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bf1822c-5abd-31ea-b31c-7df3779829ff | -0.98492 | -48.10447 | 2026-09-15 04:32:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0555d30-d671-308f-9592-572ef713b9c6 | -8.9964 | -39.98281 | 2026-09-15 04:32:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc75bb40-2ae3-3195-916d-76e881070156 | -7.54547 | -44.88994 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7138c894-79c5-3860-a888-e356d0ada7d1 | -4.52205 | -54.97042 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aec913cc-45a6-3c07-906e-7ec401b09dc3 | -3.77373 | -51.34793 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5ab84b3-ed34-37df-a06b-82b648b8127e | -6.36102 | -55.83307 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e97e76f7-ec1b-35b3-b0d7-378dc65f04ab | -2.3258 | -47.20237 | 2026-09-15 04:32:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7637cec2-85cf-3508-b46b-bcfc326f100c | -3.07952 | -50.57271 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5f6c57b-b06b-3a57-935f-4ae500b69a55 | -6.10643 | -44.07116 | 2026-09-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13af8b68-10f2-321b-9fb5-996abfa5c179 | -5.85537 | -51.94775 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9cdc694f-7511-3f1f-b846-4d982eb2bde3 | -1.23331 | -54.09339 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88b188d2-caeb-3394-a7b5-3c468ab7256c | -2.9148 | -50.42883 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b2a6fc33-8b16-3cc0-9bc9-002642003fc8 | -5.13242 | -55.9551 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e741d04-6c34-3827-9d0e-467abeb5783e | -3.07482 | -51.20259 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce0e2915-80b5-3927-926a-1822a238020b | -7.95963 | -43.98502 | 2026-09-15 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25cd396c-1246-384b-be84-29364c4268eb | -7.17462 | -43.61092 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4b2cc20-479f-30ed-a116-27f02976c6b0 | -6.5258 | -42.24767 | 2026-09-15 04:32:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| acf38629-e2a0-36f6-baa6-6f61396ea644 | -6.82997 | -43.52034 | 2026-09-15 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de53acd2-550c-37e7-bb7d-50b0ced2e2b4 | -4.66685 | -42.08469 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 40eb6a3f-8f4e-37cc-8cb8-245655008796 | -0.16342 | -50.40712 | 2026-09-15 04:32:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa83199e-502e-3ca7-845f-a915f5697644 | -3.39194 | -50.75151 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ee60c89-9050-3560-877b-9d4f6fe25950 | -2.94347 | -50.40226 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b02deaa-a400-3a16-be8c-9c19889b1d2c | -7.46713 | -46.15186 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1353586c-834d-3d68-b2da-0092a70c5539 | -2.82242 | -51.33517 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ca46a01-7f4d-327b-a863-f34ea62e54e9 | -3.37504 | -45.09219 | 2026-09-15 04:32:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6c1ad56d-d579-3f8b-b732-d372caeabbec | -7.21861 | -46.1339 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d7d9650d-4f90-3eef-9ec1-c694faa4003a | -7.02214 | -44.62905 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00296162-c7db-3006-bf0a-5a978016c3c9 | -6.61434 | -44.20472 | 2026-09-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 562d806f-86cd-3251-acb0-34263d5d3ed2 | -6.25836 | -41.97328 | 2026-09-15 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fea6ed64-5439-3beb-aaff-5e93e9118071 | -6.35562 | -55.83216 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8982b7a9-f067-34f8-a540-d95798e0cab9 | -2.96405 | -50.40038 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49507041-22b7-3759-8b9d-f89ba42b0cdd | -2.96323 | -50.40544 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8513f4b5-00d4-3521-a58d-ca89b94b29cd | -1.19614 | -54.12371 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88f92f65-1042-3c67-be67-9e0b91ee7ab4 | -3.39136 | -50.755 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a76c9918-a50e-3079-8e1b-ee09bac081cb | -4.65386 | -42.44561 | 2026-09-15 04:32:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c6416b87-75e5-30bb-947e-a0a33c6fd775 | -7.24629 | -46.17394 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7e35288-ed96-34cb-b6a0-842667a3dd40 | -8.39301 | -42.2158 | 2026-09-15 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3cf344ed-d2a0-3572-8954-706e05ff7704 | -2.9206 | -50.39333 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 836410a2-bfc2-30d0-887a-475c45daf9d1 | -6.78721 | -47.87997 | 2026-09-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4bc7782-0d2f-3a0e-9337-b5ad85866f04 | -6.61029 | -44.20798 | 2026-09-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edb24bec-c02c-3687-8e6b-54fd5132037f | -3.84448 | -51.7644 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0765bcf1-9a51-320c-b978-10faa7b24eca | -7.08468 | -42.12889 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b852cdbe-b982-3391-8ed4-e8f63ab78d16 | -4.53258 | -55.62631 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66c435e8-753d-32bd-a007-ae48a7b25820 | -5.82729 | -52.09054 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7335d4b2-238a-3a9d-b992-977df1d1714e | -3.0801 | -50.56921 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dceb2015-e235-392a-8931-d8710f69ea62 | -4.51154 | -54.96874 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c985c38-cd2c-35b3-9c23-9d3b56ff4505 | -7.24572 | -46.15602 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d34da4f2-b590-32f7-a377-4aa07fadf90a | -6.15599 | -55.71019 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 251760d6-58e8-3175-bedc-4cf145a51079 | -5.29112 | -49.0932 | 2026-09-15 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e75c276-85ee-3bea-871e-14849bb8e162 | -7.56627 | -44.91573 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af5c031f-355e-3c38-90e7-7325df016860 | -7.63653 | -46.15385 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 409fd04e-843e-328d-b14e-fb9ada5fab66 | -7.1029 | -47.48324 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e690a12-efcc-3bc4-ae73-427f95b08788 | -7.08783 | -42.13447 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a4e2433-43f7-3868-8446-e4aea79d9565 | -4.66754 | -42.08009 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| d318ad8b-6827-367d-a5eb-e199dc061a1a | -6.95424 | -42.55813 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b2d47d72-38ae-3eb2-a33e-78f29c49d52f | -5.85483 | -52.10769 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b84007-76a8-386a-a0de-7bc805ff9521 | -7.10937 | -42.09738 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dc02acf-f9e6-37b3-aa3c-49146605bb50 | -7.19775 | -45.91965 | 2026-09-15 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b20d63a-ee48-3639-af3b-651842354761 | -2.90875 | -50.39145 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42d34c71-2ac2-3a2c-a794-4f897f2fd287 | -2.95219 | -50.39849 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddd41c5d-844c-3dd3-b3e5-7390b22158ca | -6.55455 | -51.19743 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b3e2c95-7b57-357a-983e-28827a500c14 | -7.1332 | -42.12863 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 20a3c3e9-eaba-3956-90c5-baf675975039 | -2.93245 | -50.39526 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01efdaf2-3c14-3e6c-b4a5-6f19d2cb1a90 | -5.12748 | -55.95063 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02022c1f-3389-3bcf-a9a8-b14a480910a2 | -2.89113 | -48.27689 | 2026-09-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4de45b63-90ba-30dc-9860-5b9cecebdc79 | -4.66307 | -42.08411 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 56c32959-4954-3409-b085-4a664cbf8d80 | -6.14927 | -43.81476 | 2026-09-15 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19f14055-11fd-3324-b1f5-4becde2dbcda | -4.51942 | -54.92347 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3680a8ea-0367-3097-ad92-4968f818ce75 | -7.16808 | -42.10847 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6d49188-8de3-3612-b874-8f4f06176243 | -7.36437 | -46.54504 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cfb012f-ca51-3fd7-a744-95a07f221afe | -7.24242 | -46.1769 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0525a2d0-aa1e-37f8-b4fb-09f103926df8 | -4.51996 | -54.92025 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42141e2b-30a9-3c61-b9a1-c82d7727a4e9 | -4.51084 | -54.97504 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04bbec46-845a-3d58-9227-81682fd9a92e | -3.58562 | -58.55032 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06da3683-06ea-3c02-87d5-df02af245e83 | -2.32241 | -47.20184 | 2026-09-15 04:32:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f51d1b49-e5c7-361d-8bad-67126413fbd0 | -3.4115 | -58.22 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 524e15ec-e7da-362d-bf74-28882feead85 | -3.77312 | -51.35169 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f9e75d7-5389-3ec8-bc72-7e378bcfc372 | -7.61533 | -47.29641 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae7f4537-3046-3e95-aba1-273246306eb8 | -3.5402 | -48.18091 | 2026-09-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bacf28f-b99a-3988-810f-a080d69600c6 | -5.13305 | -55.95147 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be79c858-2487-33ae-9e13-2a74347189e6 | -7.46049 | -46.15082 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bef671c2-597b-3527-a3e5-19983c7b7fc9 | -2.91875 | -50.42949 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e9530c5b-47ed-334b-b8c0-2a62a3102462 | -7.55456 | -46.86687 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d2791c1-3ffa-3e1f-a13f-2d37eb53425e | -6.43111 | -43.0683 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0da0e046-dde1-3c33-9151-0b19e0d9b562 | -5.12812 | -55.94699 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44c4d3c1-2bcc-3c17-a322-12cdbd98924f | -4.08668 | -54.42928 | 2026-09-15 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a27756d-7d0e-3df7-b2ba-ed911592b52a | -3.54777 | -48.17815 | 2026-09-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2345ab09-f7ed-352d-b4b1-2d2a20734707 | -2.82118 | -51.34292 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cc71136-a7af-3f70-9503-372d0482002d | -7.16913 | -43.52564 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ee9b33f9-4344-3ac1-ab88-35928838c72c | -5.61297 | -43.56313 | 2026-09-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7ffbb5f-c6fe-3d84-8574-86c3360cda78 | -2.91563 | -50.42374 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e34fa4f4-ec07-32eb-a210-84db878803a4 | -3.91347 | -54.52109 | 2026-09-15 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f122dceb-a619-3123-91dd-284341a3ef25 | -7.24297 | -46.17342 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README37.md)

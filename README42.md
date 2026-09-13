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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edaf4704-9bcc-3e83-9bee-3d47ab218346 | 0.1471 | -51.49282 | 2026-09-13 05:08:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf0edbc1-2e06-3836-a6d8-09ea918131cd | -1.39505 | -49.34809 | 2026-09-13 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6c73eaf-2af0-381d-9c09-e02e3be196e9 | -2.11875 | -47.11769 | 2026-09-13 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fbfaea36-9def-3ced-8aab-8742ed90bb18 | 2.51063 | -50.84486 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1746e198-1c2b-30d7-9d7d-61426301d3a0 | 2.66842 | -51.03917 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25f7d7f5-5045-309b-b974-5477afa7264c | 0.96976 | -60.41106 | 2026-09-13 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26ae901a-2265-3069-a6e3-29b49c1f5f22 | 2.66763 | -51.04042 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08c08197-a4cb-3646-aee3-e443622df642 | -0.7343 | -48.04131 | 2026-09-13 05:08:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2f7ea4b-b974-395b-bf9c-9447d009f4dd | 0.1461 | -51.4637 | 2026-09-13 05:08:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7212e53d-2b28-342d-9633-bd73be896edb | -1.03004 | -53.73869 | 2026-09-13 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edba8b72-7533-3ce0-bec9-0615a94124a4 | 0.14676 | -51.46777 | 2026-09-13 05:08:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c197cda-725e-3c11-9c37-1bc89e8b5b0b | -1.0267 | -53.73817 | 2026-09-13 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0acfe984-bc78-394e-9623-201fac5a1b9e | -1.87479 | -47.91224 | 2026-09-13 05:08:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bdff38d-c8fc-3c23-bd4b-0b81f0f1c518 | 3.97555 | -59.63791 | 2026-09-13 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69cce1dd-5e4c-3921-b490-781f093e0c8d | 0.17512 | -51.48429 | 2026-09-13 05:08:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1de3edc9-b2df-3418-b3d8-6153e49ebc91 | 2.51489 | -50.84845 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7cd7f6a-10f2-364c-ab59-2b90d3d8ed5b | 1.06252 | -50.96583 | 2026-09-13 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6a0fdc1-57dc-397f-b45b-9f54202cbc4d | 2.51195 | -50.85315 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a34f754-3653-3362-9044-178432ea183f | -1.02949 | -53.74215 | 2026-09-13 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ee63ba8-0a73-341b-9503-3c454ee43173 | -1.87553 | -47.90742 | 2026-09-13 05:08:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 424b234f-b9ed-39ec-988f-21b46af12213 | 1.06549 | -50.96103 | 2026-09-13 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 969a7e25-c2a7-3889-a24a-5a9febc89c7c | 1.06913 | -50.96046 | 2026-09-13 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5aea06d-c451-3ff8-a3ed-31c60e533f9a | -1.3783 | -49.41597 | 2026-09-13 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 551643c3-42fd-3f30-aaee-fbbd143a49c0 | -2.11386 | -47.11683 | 2026-09-13 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e19ab37e-2fe6-303f-adb4-960a2a45fac1 | 2.5126 | -50.85728 | 2026-09-13 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3e5cb95-e59c-3690-976a-e1d27937170d | 1.05888 | -50.96641 | 2026-09-13 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5d102e1-76ff-3a18-bddc-ac36ff4a643d | 0.14969 | -51.46314 | 2026-09-13 05:08:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e40060c-c127-3b2d-ad89-362e36ae85f2 | 1.32343 | -60.71202 | 2026-09-13 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11754376-5965-3548-a3db-eb03a047d9cb | -1.79251 | -47.83772 | 2026-09-13 05:08:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e48765be-22a7-37c6-9c21-46f733bf874a | -1.19084 | -55.72444 | 2026-09-13 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a94e3d31-19ae-3ed6-bd38-67696b2d1db7 | -6.81529 | -59.55859 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93e66de8-dde4-3257-8972-9dee409ab299 | -7.9669 | -43.99504 | 2026-09-13 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fe0a96d-e9a5-3e47-870e-696fca774fd9 | -6.09175 | -57.6862 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d54e828d-94b0-323f-8ea4-e7e573158766 | -6.86123 | -47.42692 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ab7a686-0a0c-35c1-8920-d67bb42e7913 | -1.22277 | -54.12878 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9a22fc7-b539-37da-9fe5-e665eca0c2f7 | -2.66983 | -57.53173 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e8a91dbf-563b-3e14-8191-8435f460957d | -5.98832 | -57.69698 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 368fc186-1ee0-3d40-a5a3-85048c826053 | -3.8943 | -55.81713 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401d9a44-ad16-35e8-8361-3a43a75275d7 | -6.59385 | -58.85012 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95e4cf65-f2e9-33b2-9f75-f0b1357ecc08 | -8.21037 | -47.86647 | 2026-09-13 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce39c6af-b58e-3508-9b75-cefdef93c1da | -2.72247 | -49.79048 | 2026-09-13 05:10:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba78003b-5765-32f9-8778-96faeb8761bb | -7.9676 | -43.98955 | 2026-09-13 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d2beb5a-4081-31d0-8f24-a343d86ddf46 | -5.12409 | -55.9662 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c702dd3-7ca7-37ed-b9a5-a07adffd46b8 | -7.87237 | -54.7219 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 316cf357-4280-3c02-b638-036e66816c51 | -6.08467 | -57.85954 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 638ee668-0a16-3c03-b97d-a9e08abdbbb9 | -7.86331 | -54.69051 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32d28adb-71f6-317e-8c0e-25639b5d9586 | -6.37611 | -58.29364 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f96a03f8-e3c4-3a47-ba23-e7bb05c0372f | -6.76576 | -59.42679 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9e1cf21-fcc8-333c-91e1-7db18dc0c4ae | -6.10611 | -57.66226 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b11a270a-6f6b-3a26-8ab1-787e2fbb590b | -8.5461 | -54.71162 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aea5d8a-6901-309a-af34-093cb69c5717 | -6.74564 | -59.43415 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 975d8d24-d474-34ee-8817-1c94dd0e5ff3 | -3.82166 | -59.22225 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28caeb7a-9203-3c9b-82dc-44fe071be107 | -7.46859 | -46.14763 | 2026-09-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 96ae7699-ef06-3671-a9a5-a6f65c221d67 | -2.96636 | -50.41082 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 217a9fec-de70-38b8-97cd-f40e61dd6cae | -7.87124 | -54.72923 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8d1c59f-605f-3538-9eb1-ddae1349f868 | -3.04877 | -51.26333 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf2646aa-c466-36b4-bbcb-db272c02eb30 | -9.37925 | -50.1135 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e19c090-1f07-396e-88d7-d475c98c60b8 | -6.02337 | -59.94146 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd850529-1b53-3ce6-b81f-e604c5be9e81 | -6.57583 | -59.0056 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75c52b84-a3fc-3387-bd4d-0fc4b7505ece | -2.94172 | -50.41226 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8447b863-1c02-3320-869a-593ab015e3e4 | -7.37963 | -45.34972 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c2a7bac-c791-3647-876b-bce8047e7acd | -6.11232 | -57.66702 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 7828d59a-6ef1-3723-b72d-7341215df83b | -7.96037 | -43.99397 | 2026-09-13 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bde3e00-ebac-3087-9d0b-2b597032b969 | -6.22947 | -51.69238 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6febf18-15b4-310f-86e1-ce351f40dc26 | -6.10951 | -57.66282 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d9155ade-408e-3285-acd8-feab332935a9 | -4.08223 | -56.3024 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83bdcfc1-c79c-3357-9791-abb16e9cae79 | -7.07989 | -49.94279 | 2026-09-13 05:10:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e23c159-0da4-3897-8f73-e7212a1298ea | -7.19641 | -45.92249 | 2026-09-13 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09a822e9-7f44-32f5-9302-c76b64170c14 | -8.05591 | -54.84996 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1183c3af-a0b1-38ae-a6cd-cf1538fe8e8b | -6.23447 | -51.70059 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 488b1076-b5e5-3484-986c-9af5f5b74254 | -7.01962 | -44.63506 | 2026-09-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9afb858-340a-3208-a41b-6f41d1b39fbb | -6.06975 | -57.86482 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1feae12-f072-3cae-963f-4be3d5c909e4 | -6.18858 | -57.71706 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d304e72a-1460-3fee-9c2b-cdbbb7842f14 | -7.13237 | -43.75505 | 2026-09-13 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee5ddaf7-3c1a-3178-bf13-bdace26abb4a | -6.22874 | -51.69712 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9eb2711e-3b74-3f9d-bb46-ebaf18ba76af | -6.50934 | -47.5989 | 2026-09-13 05:10:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c955e213-4c60-312e-be79-56332a722abb | -6.69681 | -59.13433 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 088ccd60-a435-3dfa-b196-204c046c9247 | -5.77246 | -45.09709 | 2026-09-13 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbea447f-20f4-3d5a-bb2a-6582eac2f335 | -3.82875 | -51.88856 | 2026-09-13 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4bb8d4c-ba62-3f26-bf5c-8f232c7434de | -3.40597 | -59.25164 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dc0697b8-796d-352d-b949-98e34e94f1de | -6.6045 | -58.85186 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01069156-fbf7-3c90-9d99-1d05a819b8b2 | -7.42821 | -55.52851 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d16a2394-10f0-3615-82bd-b62a1a53be67 | -5.98653 | -57.70806 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9e1de9b-b07a-3d34-9f48-cd31f0039690 | -3.04553 | -51.26093 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de09fb2f-541d-3086-a62d-d3d7fc34dcfc | -6.01243 | -57.8299 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9d7381f-f6fa-3649-ae17-34aa3623f040 | -8.03114 | -54.85353 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 564163fd-a901-3c89-8d14-4705ea2ff9ac | -4.54952 | -54.91642 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b931b56-cc0f-318d-a549-de31eac67167 | -6.30986 | -59.99157 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9f3029f-5017-3b6e-a34a-522c22d0fde4 | -2.94966 | -50.41352 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 148bd899-d2ed-394e-8a47-b2e7126c38e4 | -3.04266 | -51.25306 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0463961e-6fb2-36eb-85fc-6077764e0042 | -1.73288 | -55.24205 | 2026-09-13 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c6e09cd-765d-3804-8c1e-65537cbac417 | -8.05198 | -54.85306 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b03d3ba-7584-3ea3-8f24-7c70c433d0c8 | -6.34127 | -57.87795 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6623297-8007-35ab-ab89-f915c82bd20f | -0.97649 | -55.38477 | 2026-09-13 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b07d032-7608-3e96-b7c8-91d2c56fcd45 | -6.85519 | -47.4322 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a153e65-d3fe-30e0-932d-79e3b13be8a6 | -4.72946 | -55.73399 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b690d24f-f954-3039-bed7-befd360b0d51 | -6.27668 | -59.93405 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3fb52d0-9152-3746-a90e-f33f4e7e9326 | -2.67844 | -57.54494 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 85366831-957b-30e7-849c-89cb77943dab | -8.0486 | -54.85254 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13dad7c9-eb74-38cf-b9bf-c2abcb1034ae | -7.75505 | -49.4432 | 2026-09-13 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)

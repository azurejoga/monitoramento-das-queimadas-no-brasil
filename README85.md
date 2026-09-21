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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| effe1a12-1126-3013-994a-4c5a172819e5 | -3.52624 | -59.89118 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c882c6f-0443-32fb-8b73-a3c9b8070028 | -3.00063 | -54.167 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e1c705a7-6e62-34c0-acc0-f5230b8eb258 | -3.36352 | -61.30038 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b5baef-4eff-36e0-8c06-285baaeab55a | -3.13506 | -61.22566 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd7a25a7-db40-362c-9a5f-655d3bf3c60c | -4.88056 | -55.88313 | 2026-09-21 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9afe55d7-8914-3d10-b9ac-3735a878ca96 | -3.49026 | -59.6077 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 260a76de-2209-3c2d-b130-6757f8b2f668 | -3.42569 | -59.26051 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 414436da-e082-3e77-8e8e-7660bfc0d934 | -3.7532 | -59.42131 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0244d43-7f01-3aca-bbf4-8049360763f4 | -3.64167 | -58.86455 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39a66194-a68f-3140-8fb5-350921901bea | -2.69997 | -60.96249 | 2026-09-21 05:40:00 | NPP-375D | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37c16b16-5793-3e5f-b794-5e0145f7e4d7 | -3.78787 | -55.8779 | 2026-09-21 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 547f419b-e1ec-3625-974c-f0f5816b1098 | 1.21899 | -50.97863 | 2026-09-21 05:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d57004a-6f78-3899-9b2b-39c57687b9ec | -3.06252 | -61.27811 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1232d2f-2b6b-32ac-96ef-42d8804fadfb | -4.26305 | -55.77005 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1da7e874-eccd-30f1-babd-91c74a08b0e0 | -3.33803 | -59.80275 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 827133e9-3925-3001-8551-c61208de85b3 | -3.66232 | -54.26961 | 2026-09-21 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64636a65-9fe4-35ef-bcdc-77b671e74076 | -3.48286 | -59.56479 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd9f0d42-3464-335a-a7db-25fd0c7236d5 | -3.17361 | -58.58979 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4712c733-3091-365b-8561-c2309190d529 | -3.8945 | -52.11892 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11acb3de-cc5d-3514-a098-2d042642b30b | -3.32952 | -59.81261 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6c6659d-cfc4-3ce5-842a-7926bd4b472d | -3.34144 | -59.84804 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73708863-b42d-3390-9157-4edde871ca37 | -2.87542 | -57.82194 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fca09c2d-677f-38a8-b2e9-3811e71fb7bd | -3.08004 | -61.16758 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fd162e5-fa35-3eba-bf8b-f66e48f1aa8b | -2.60109 | -59.7609 | 2026-09-21 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21ec0aff-2770-336a-aee5-a5b71ba5e275 | -3.05532 | -61.28052 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2a664bc-2e28-3ea9-8f4f-46ec5f6e2fcf | -3.44289 | -58.22884 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 131da400-3275-35a4-a9a2-7bec57cda629 | -2.86877 | -57.80526 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 96ee92e7-180b-3493-89a6-e4a2c5246af8 | -3.33293 | -59.83553 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2d0623c-065c-3181-aab3-4245b1206722 | -2.8632 | -59.86795 | 2026-09-21 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e53ccaff-4cc0-35ca-a7b7-b1822d79e440 | -3.39123 | -59.52838 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b38fd7d1-d64c-366b-828e-86c805bd1f28 | -5.01254 | -56.08701 | 2026-09-21 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68a8a043-e2b8-399c-8166-dac27944e0d9 | -4.40877 | -55.23995 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79d37e16-34e8-39c1-9c51-41f21e64e0c0 | -3.33478 | -59.44398 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a61a861b-bcd1-3639-94ea-46759a600735 | -2.45913 | -49.2191 | 2026-09-21 05:40:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 082a7f5d-841a-348d-bf51-307fd30ce004 | -3.05642 | -61.27361 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b03e5c2-dc69-3740-893f-b91f34ad1a60 | -2.16721 | -48.32523 | 2026-09-21 05:40:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 237212e1-14d3-30f0-8fd2-8a3a737cd73e | -3.38488 | -50.43694 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f4f539e7-1664-3a1f-827a-206cfce61f81 | 1.38472 | -50.92318 | 2026-09-21 05:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf4cb518-3bf1-3e26-8ca5-54bf6b0d0fd8 | -3.48625 | -59.61087 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a85d7070-e774-3d79-ad3f-35e5b7ad8397 | -3.43809 | -58.01904 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75536a54-5933-39bd-a656-3a9c7037c515 | -3.68744 | -60.59958 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccf96b00-5a66-3578-9322-d35d63174761 | -3.80034 | -60.72116 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7ca9836-8603-38cd-92d8-929c13e217f4 | -3.40118 | -61.29921 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5062243-cf44-308e-89e7-177c2b7c9025 | -4.21908 | -59.41306 | 2026-09-21 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85dddee6-176e-336c-9649-9f85e49197fc | 0.79201 | -59.20552 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62fc5104-675c-3c91-82a7-d5a6460dc43b | -3.40505 | -61.29628 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 467f8116-aba3-387a-9a3d-d4f9c0ee8332 | -4.68189 | -55.62984 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 262b69a7-4b6e-308f-aea8-001ad59f58b7 | 0.94443 | -59.52972 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b61d9018-1fc2-3fb3-928e-9a84741430f3 | -2.95786 | -57.97135 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3abb256c-b3b7-39d0-81cd-1ab6745d1026 | -3.22451 | -61.04832 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65d919da-d379-35f7-a074-4ca9d8dd8445 | 0.7847 | -59.20301 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8b0dca1-1eea-33a1-944a-6d2b158eb789 | -2.90446 | -59.22588 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e013b382-c471-31b1-ab24-9bda1a7634ec | -3.53903 | -58.69102 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1078753-6069-3fc9-b301-2ce186269899 | -3.79885 | -59.71129 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e369925-dfe6-3852-9143-6b557976208e | -2.45357 | -49.21541 | 2026-09-21 05:40:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ebb6188-df94-30aa-b9ab-bf5c2f557734 | -3.233 | -60.80075 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af9fed98-5165-3ea6-91bf-2b7d636e029e | -4.35058 | -55.65574 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 782733d5-b0f3-3760-9e7a-05b3cfb13188 | -3.82246 | -58.88204 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c828a493-2900-3d0a-bd49-2701f989736b | -4.34625 | -55.65505 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3e58727-5bf0-340a-b14f-487f98a57e1b | -3.68301 | -60.62769 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26c86436-f228-34f8-bb8e-0759e74a2dae | -3.10641 | -60.72047 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a8d397f-3dfc-3252-8fbc-0ff8c78cc9b2 | -2.85705 | -57.63717 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f35e51bc-81d3-3ad4-bf50-0db896a3db08 | -3.48911 | -59.61511 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8e6a0e2-8098-3800-af4f-e8bec3454522 | -3.54321 | -58.68757 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe8c84c3-6268-3571-a4bb-43ffe590323e | -4.09679 | -52.11696 | 2026-09-21 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3c2ab9f-f682-3122-8a12-3d2e087ed7da | -3.48969 | -59.6114 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 043d383c-5b25-30c0-ac40-17045a298fc0 | -3.17388 | -60.35751 | 2026-09-21 05:40:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93da1ca7-d70e-3a15-b690-524f677c7d4f | 0.26537 | -51.00026 | 2026-09-21 05:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2326bebc-4a01-3d3e-9425-4ebd800640aa | -3.38423 | -50.4414 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 906ea76e-6ba3-34b0-832c-45d8210c1eda | -3.39666 | -58.47625 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4c01972-5686-3eb1-9066-1ee37a061f97 | -2.90723 | -54.18994 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db4fca64-ce36-31f1-957c-56335da2e64e | -3.00531 | -54.16783 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fe30b22-93d4-38d4-ae3c-643ce5ca0104 | -3.0132 | -54.17942 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a15eea1-562e-301d-88ba-30a036878401 | -3.31409 | -59.44078 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9858d483-fef3-3cd7-9b39-d5a207e4f5ab | -3.06654 | -61.05918 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5369f507-4203-34de-800b-1a4bcb31f7fc | -3.8288 | -51.19863 | 2026-09-21 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6531ee8f-bf28-3e9f-a4e9-271b9b96e230 | -3.46074 | -58.40123 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bc1f959-bc8d-31c9-8d66-952ce34833fd | -2.79427 | -59.88678 | 2026-09-21 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8120b034-497e-3216-bf4d-f63d4f81ab65 | -3.88901 | -52.11818 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac17b644-5135-3405-8dcf-9356c3c178c2 | -3.64751 | -58.87356 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa94c615-2065-3aff-baec-29ffaab07692 | -4.22607 | -48.61775 | 2026-09-21 05:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f177e87e-4a14-339d-a92a-ab379e6804a9 | -3.87828 | -59.56374 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f94242a9-8ec1-3f06-9be4-63197f2ac3a8 | -3.82417 | -59.33141 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68abadd3-32e6-30aa-be78-8676792faf98 | -2.79088 | -59.88624 | 2026-09-21 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 660b55e9-dd04-3e91-9141-eb6faaf034d9 | -3.17307 | -61.11473 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a41d66e-9334-3e9e-95fc-0400b90cc6ef | -2.90504 | -59.22213 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de6461fb-ae94-30e5-9a08-a731875cffc2 | -3.40783 | -61.30025 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b7df397-8ccc-3669-b726-b10139c108ca | -3.5224 | -58.58515 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 572b442f-8436-3a98-acd1-ed2d4982b90d | -3.12657 | -61.4296 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc076bfb-efd5-3cd7-b83e-8fdb57f704d4 | -3.04037 | -61.58959 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4fd187a-301d-38e5-98d3-b6c3eca95237 | 1.66153 | -50.92838 | 2026-09-21 05:40:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8b0a26e-c31d-3e3b-85ab-555b2997df79 | -3.06916 | -61.27915 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c79af2a-788e-3434-ba7c-695d03fccc70 | -3.42178 | -59.19354 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b24da8e-57be-38a3-bfa9-5a5c1e18cc4e | -3.33349 | -59.83188 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90fe8dd8-07d3-3ba0-bd77-4bd21d7f94e4 | -3.30599 | -57.86956 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50ff68ba-f136-3409-b804-c5a99384605f | -2.64321 | -54.68776 | 2026-09-21 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4767674-4d7a-3012-9866-d81c5dd68fce | -2.9092 | -54.19197 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1349615-bcc4-3f23-b021-92b85a1ce733 | 1.07894 | -60.67927 | 2026-09-21 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e2fcb79-220b-3ed0-b37a-45f93dab01e5 | -3.44671 | -50.60191 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b025a0f-d9d0-3748-8987-2bf4cb7a185b | -2.87755 | -57.7977 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README86.md)

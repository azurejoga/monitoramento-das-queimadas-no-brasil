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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7aed2bdd-92db-33c9-b853-853c423104b0 | -2.95095 | -54.15781 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6cf8ddd9-1662-337f-bb65-e3575d4fa5af | -3.68059 | -59.62492 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b800b369-f4a9-38c9-994a-510d8347207f | -3.17242 | -60.06088 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e2834561-6449-37c7-86e4-db675cc6544c | -2.18492 | -49.7539 | 2026-10-05 17:17:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac90fe00-a99c-3655-b8e5-5226c3a3762d | -3.09119 | -65.01089 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e30b812-2ead-3400-82d8-4aaa3ad980e2 | -3.41607 | -58.42424 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f826d707-b5a4-3bc5-93cf-e2dc88663d42 | -3.54826 | -59.48624 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 185b5296-422b-3174-bf11-19c29cd689cd | 2.26503 | -55.95774 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3391e0da-d44a-3f34-b9f0-19f46a520163 | -1.19518 | -55.69564 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d1fc86e5-2109-370c-ad4d-64bf6f0f9016 | -1.33756 | -55.96537 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 48fc44b5-a558-3b9f-8034-fb78ee6e1aec | -0.38101 | -52.07756 | 2026-10-05 17:17:00 | NPP-375 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.1 |
| f57ed6fc-c309-304f-a108-47d8b0a07667 | -3.51394 | -59.55448 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c64fdb95-8a14-39e0-bce3-2b9fc1fbc9d3 | -2.09891 | -48.86155 | 2026-10-05 17:17:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3a343070-e443-3985-8f46-004b63bb9123 | -2.86748 | -56.89805 | 2026-10-05 17:17:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9c2dd468-6ced-3748-9356-8af0b51c5adc | -3.49298 | -57.64338 | 2026-10-05 17:17:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e77658e9-f452-311c-b098-ffc410953934 | -3.21026 | -56.83184 | 2026-10-05 17:17:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| efc39e18-dffc-39ce-92c3-0fd005bf179d | 1.45771 | -55.66388 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| c8d618e0-e8c3-3425-88b3-daefb44a1ee0 | -3.68387 | -58.88559 | 2026-10-05 17:17:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 378e8ec6-484e-3b60-900f-b0b9165f126b | -3.27082 | -59.5946 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fe49774-2350-30ec-91da-105e5a4c5d65 | -2.98614 | -65.18478 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28fc4601-29df-3bf8-8f37-5708275ee2ef | 3.52751 | -51.51147 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8c58bbb6-2bd3-3f75-841a-14d7cc17d43a | -1.17976 | -49.24489 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 38b335c2-f9ee-3133-8ac7-80d2f83d6924 | -3.23901 | -64.83919 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 49a007dd-3003-3585-bed4-1de24499cef8 | -1.66977 | -55.46394 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 99c1edb9-baa3-35df-8ff4-a94ac1e50615 | -2.38746 | -56.12268 | 2026-10-05 17:17:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5db19d76-357d-3cd6-a2e7-bf1f5714d502 | 1.73361 | -55.71848 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40cd9d51-f29f-3b83-b949-2c71c248c98b | -3.18454 | -60.05508 | 2026-10-05 17:17:00 | NPP-375 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d9aca0f3-6f96-343b-a0ee-0f35f8405be7 | -4.2556 | -63.64017 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| d4acc4e9-3224-318a-ae87-deef37d96ebd | 1.93094 | -55.71066 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7a6cb83-ffa3-33d1-85b9-adaf72012dc2 | 1.82955 | -55.55377 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9c265e9-8031-3b49-be7a-c6538522450b | -1.25105 | -55.88138 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00b8ee8b-3294-33d8-9c88-bc89e8fd8cd5 | 0.31467 | -51.00465 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed48b8ce-cdb1-34a2-9044-bd0a54a81a34 | -1.67363 | -55.06606 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 30b4fb97-9807-356c-9ba0-0c3adcf4936a | -1.87435 | -50.04314 | 2026-10-05 17:17:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cfff2915-4a5c-338c-9670-a604bb472436 | 2.15101 | -55.97485 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a0388d61-055d-3288-b66d-5af14369b6ce | -1.25709 | -49.32219 | 2026-10-05 17:17:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 3d3b6c58-0b0a-3fc0-a303-62cf513062e6 | -2.82531 | -54.12901 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 6f66589e-f035-3173-9fb2-a2106fba561e | -3.74168 | -59.41308 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c8c0dc7-f5db-3203-95cf-78af2dc7c799 | -2.02289 | -56.88866 | 2026-10-05 17:17:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22f1e6ea-1b24-3c60-b633-b3dfe39548b1 | -3.22907 | -57.12371 | 2026-10-05 17:17:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| aa6873e2-0fd8-3a9c-9321-2eaad8cf1c76 | -3.71036 | -58.92804 | 2026-10-05 17:17:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 251.5 |
| 51b9b7b2-40ab-3621-9203-43dbbf3081d2 | -2.93222 | -54.11916 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f4f9b0e6-af9c-319a-82d1-a2f0474ca6bd | -3.37037 | -58.1949 | 2026-10-05 17:17:00 | NPP-375 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1ef02cd4-c119-33b8-882f-cbf74789352c | -1.64486 | -55.14463 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2860e0f2-040e-3e25-9e1d-560ffdca140f | -1.61669 | -55.13828 | 2026-10-05 17:17:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c5efc9d-349e-3323-ad7f-2a0021c000f5 | -3.81936 | -61.13059 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 14764e30-784f-3072-97c9-1b7ccb123e57 | -2.34228 | -57.11871 | 2026-10-05 17:17:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 932dd522-5218-3135-9d7e-629d99f53486 | -1.11759 | -47.73819 | 2026-10-05 17:17:00 | NPP-375 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 65ed3120-02c5-3dd0-9a18-36bb0281dbcd | -2.94572 | -54.16304 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 5d523a3b-eab6-3049-ab66-4cb4d5019cc4 | -2.94844 | -54.11933 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b4c67633-6675-34bb-bf27-3614d4d98b61 | -3.00122 | -54.24197 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a51c766-010d-325f-a382-93e4558a050e | -2.96452 | -54.11336 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bf64e0b9-33da-309c-bbf3-7a8be65aafe6 | -2.13232 | -56.69004 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f1a188fc-c529-3348-9af2-30cac85eb12a | -3.51559 | -59.56547 | 2026-10-05 17:17:00 | NPP-375 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 469383f9-fb73-362a-866f-6098873ace1f | -3.6911 | -59.63874 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b161388b-c74b-3fed-8b50-a76355e5e7eb | 3.5321 | -51.50721 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 90802c93-ec73-3631-8d99-ebbad2c84eec | 1.91384 | -55.7116 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f13d0d5-0d16-32ad-bf37-91fbe29bef69 | -2.92543 | -54.14139 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de3bd1b6-592c-30dd-9bcb-aa268a8eeaff | -0.83298 | -49.28617 | 2026-10-05 17:17:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c5a887f-6ebd-3762-b822-e811740d669f | -1.48577 | -55.16594 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0929eda9-6e0f-3c62-b4ec-a746ffb4c33b | 1.31656 | -51.15176 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f7d81c9-4472-3d5e-889d-34a1519bd51a | 1.63427 | -51.00288 | 2026-10-05 17:17:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 89ea657d-869f-3baf-9883-fa6b63b2f3f5 | -1.86414 | -50.60406 | 2026-10-05 17:17:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 369968ea-28dc-3931-9e30-d3e036880187 | -3.53255 | -59.40718 | 2026-10-05 17:17:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9530527d-966c-3bd4-b34b-cdc253f01230 | -2.9702 | -54.17255 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 686fd9c6-93e1-30e7-81e0-73f5e51ab03f | -0.25713 | -48.67251 | 2026-10-05 17:17:00 | NPP-375 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 115efb9e-7665-3b7f-bf54-2738ea46b840 | -1.38145 | -55.40943 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 32f03738-1b54-3549-9fce-84481b0e5e3f | -2.02671 | -54.32521 | 2026-10-05 17:17:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9efa398-0021-3d39-b000-473cc5a6ed2a | -3.64915 | -60.92082 | 2026-10-05 17:17:00 | NPP-375 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b01700c2-27fe-3e2e-b7c8-38929ec3f068 | -4.32238 | -63.44318 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8634ecfe-758c-3289-a55c-e7ffb6b83d58 | -1.42882 | -52.72983 | 2026-10-05 17:17:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c65e937e-b3f5-3ce3-8dbd-67f7949695e5 | -2.92596 | -54.14484 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b95d330a-0270-396f-8edb-3aa9b9b714d2 | -1.34151 | -46.86729 | 2026-10-05 17:17:00 | NPP-375 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfe3e8f9-6456-37b7-b899-23adb9d6c066 | -3.58046 | -60.5391 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f1d6e898-a4eb-3a37-883a-ea29a98e03f7 | -4.25611 | -63.64379 | 2026-10-05 17:17:00 | NPP-375 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 2c87f653-fcb6-3410-811c-e70f18e74543 | -2.44079 | -58.01625 | 2026-10-05 17:17:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 44dd9d74-9ff8-3003-a6c0-509c6f661f9d | -3.39869 | -57.23933 | 2026-10-05 17:17:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f6daed5e-44b7-3c30-be18-80a48cf0dff8 | 1.80742 | -55.54656 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f630c56c-70ab-3cf4-a3ae-e04fdfff1b20 | 0.67004 | -59.98685 | 2026-10-05 17:17:00 | NPP-375 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bf383827-5f8d-3966-90ef-f2a366293fee | -3.45479 | -60.56434 | 2026-10-05 17:17:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ee1f8a0-b13d-33da-b355-9cd5df920a70 | 3.53139 | -51.51205 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c74483ab-fe3a-30ad-9305-17d004677e0a | 3.54374 | -51.50898 | 2026-10-05 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3cf23106-8ec1-3ed8-80fd-0161f7d379a4 | -2.98905 | -65.2212 | 2026-10-05 17:17:00 | NPP-375 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d445ec37-200b-3d74-a249-d77471825cbe | 1.79695 | -55.54849 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d09bf0a0-8c69-37b7-b75d-a37b1ea19356 | 1.75553 | -55.61964 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6b58b751-9d57-3a01-929e-c56cee487c0b | -1.36045 | -55.98006 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9cc3fe8d-1c30-3aa9-92dd-cb35a21745eb | -0.71996 | -57.96943 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c1a91f0c-d51e-3d38-a03e-314be83c9201 | -1.92615 | -56.75586 | 2026-10-05 17:17:00 | NPP-375 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| eefda8d3-d3a8-306b-a404-bd3abb88ea66 | -1.74834 | -56.02562 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a42a7d0b-1a02-3ec9-b9d1-741612c71219 | -2.95985 | -54.1494 | 2026-10-05 17:17:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fabf8a0-d463-343e-a617-51e814b0bf2a | -3.84316 | -61.29354 | 2026-10-05 17:17:00 | NPP-375 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 661b8e3f-7ac0-3c95-a102-acc15d2e7e80 | -1.69728 | -55.0229 | 2026-10-05 17:17:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 752d42f0-fa38-3ac0-afe9-592c310b8f75 | -3.2856 | -64.80296 | 2026-10-05 17:17:00 | NPP-375 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c5143289-a27a-3e55-83b7-285421173a54 | -2.99125 | -57.89721 | 2026-10-05 17:17:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 00f1484a-5f2d-35e8-a88d-245a67d656ac | -1.29262 | -55.71607 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8874695b-fb02-3fce-9584-b3bb5b4e4e17 | 1.29423 | -51.13104 | 2026-10-05 17:17:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a97309a6-8cd2-3931-82d5-e28362860304 | -1.35373 | -55.98108 | 2026-10-05 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 06e9e414-b414-3903-a399-8cd5245aa445 | 0.30845 | -50.99416 | 2026-10-05 17:17:00 | NPP-375 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fa1f9eb3-735a-3e6b-b89d-691c671bf7b0 | 1.51584 | -55.6382 | 2026-10-05 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32d2ef33-46ba-3424-914e-6b18d269cff1 | -3.19818 | -57.08741 | 2026-10-05 17:17:00 | NPP-375 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README126.md)

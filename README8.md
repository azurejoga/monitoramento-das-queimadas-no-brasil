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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43c8047a-3f3b-3907-a7b3-cd97ec5c67ab | -3.8061 | -49.939499 | 2026-10-09 00:06:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3ed6e3b-1c77-319f-a406-5466fae0517f | -1.5385 | -54.559101 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fe8ba2e-98e4-3b39-bc22-d7b9319f03e8 | -17.003599 | -41.176701 | 2026-10-09 00:06:00 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6b5036c-0276-3449-ae30-9fc49fdd34a8 | -3.6045 | -54.663502 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06133926-d198-353a-97ec-09d2eb559e33 | -3.3032 | -49.127602 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8676b2b6-e055-31b1-8934-25dda8023e88 | -13.1485 | -54.343399 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c56d283e-1219-321a-8485-974a8779dd53 | -11.7824 | -45.603802 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9305ae88-2b85-3c43-a69c-6bcbee8ef06b | -7.5405 | -47.127899 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27c88569-e978-3877-9e1d-10585feea834 | -11.2259 | -45.2966 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34f970fb-294a-3369-84e1-1750d8dd5d12 | -2.8649 | -54.197399 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66a5298-d75c-33ac-8bec-7d588f1187fb | -2.4931 | -58.0569 | 2026-10-09 00:06:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 319efc27-0bc3-3213-968b-bbaadce8b4a9 | -15.3303 | -42.763802 | 2026-10-09 00:06:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe35904e-e0e9-39c1-a5ee-949b1f2143ee | -2.8683 | -54.166302 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bdf9c86-df87-3e37-bc3c-8f6a25f16e02 | -6.7424 | -55.118301 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 350aafb2-a042-39e3-8caf-d07e421304b8 | -8.7365 | -45.1595 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 371ada39-a0a4-3961-aee8-309b7ddc8486 | -2.999 | -54.107498 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbd7777-887d-3283-aa69-0ccf66e9b5e9 | -6.3163 | -54.798401 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24bbcdca-1306-3915-8eb4-06df850ec67e | -3.0101 | -57.766201 | 2026-10-09 00:06:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d541144e-ef10-357f-abd0-c71fc9f49241 | -15.784 | -44.685799 | 2026-10-09 00:06:00 | METOP-B | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f2c09a2a-c0d2-36dd-83e1-6fdee0aca6a9 | -3.5653 | -54.672001 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6a170e-5a31-3e2f-9f09-f21ae254fc55 | -5.4909 | -44.296299 | 2026-10-09 00:06:00 | METOP-B | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f82813a-5dcc-36ff-b133-9466ff029483 | -9.1172 | -48.813099 | 2026-10-09 00:06:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d057705a-864e-34e7-a5ff-4749e144559a | -6.8841 | -43.691502 | 2026-10-09 00:06:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 20699e16-1fd1-3f82-8d5d-e6f5ca045090 | -13.1527 | -54.3134 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26267f31-8d8b-34ea-b003-a06a29550778 | -3.6959 | -47.679901 | 2026-10-09 00:06:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98bab18c-651f-3990-b4b1-1d8c790067d4 | -8.7189 | -45.128101 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca021089-7fbb-350a-8363-01519eeee8a0 | -1.1071 | -54.148499 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4260c2fb-3abf-3fcd-863b-18867496a035 | -5.9354 | -51.822899 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1623f5-4d68-3712-9dd2-8a0c68aa2dcb | -8.9767 | -45.925598 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2879ae4-dba2-3dbc-bc1b-0c78ef102e2e | -5.1019 | -46.212502 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3609e83-0d40-3dce-8797-8f489d1ce327 | -11.8364 | -43.590698 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2836c512-dbcf-347d-ab8e-603530a5c960 | -13.1625 | -54.311401 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aad7a4fe-6591-38d3-ac70-cb3a299fb72c | -3.8814 | -51.929199 | 2026-10-09 00:06:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1089df-697c-3c32-bf20-fdaee4cdbeba | -3.1799 | -50.590599 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe1fb793-6e17-30a7-ac9c-bd8f2224da35 | -2.2505 | -45.420399 | 2026-10-09 00:06:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf19b20-f85f-3a59-b088-f48d3abe27e0 | -3.0122 | -54.074402 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb1cc11-3a97-353d-abce-37ead90a758d | -2.9764 | -54.052101 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a00ff2b-e958-30f1-ae6f-5bcd4b862867 | 3.5509 | -51.279202 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f5440b1b-a084-3be7-8952-8864cef83ceb | -10.3595 | -45.123501 | 2026-10-09 00:06:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78cb4533-8755-3256-83b6-b893d2770fd1 | -18.076799 | -42.259201 | 2026-10-09 00:06:00 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c9c10b9-aecb-3ac7-9fdc-96029fd5e237 | -6.0649 | -44.107399 | 2026-10-09 00:06:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4a764a7-0b5b-31fd-bbf5-9b366e6433e2 | -17.000799 | -41.1656 | 2026-10-09 00:06:00 | METOP-B | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0a53cbc-e999-3533-81c2-33680a1605b9 | -8.7404 | -45.131901 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9a2842ee-f9a7-350e-8213-7a2dfc58a73a | -3.5844 | -52.6735 | 2026-10-09 00:06:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e0f5526-898a-3c5e-b384-91639135c4dd | -2.8334 | -49.511902 | 2026-10-09 00:06:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 103cfd47-27ca-3948-bb7f-3b472f4bd28d | -1.1839 | -54.169998 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93641f5e-34b3-3358-adda-a2403049a3f4 | -5.8505 | -53.4501 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d071d39f-2592-3e98-8404-828c7053ce00 | -1.5505 | -54.5667 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5736fe84-5cb5-3cfc-b3df-40d9be478527 | -3.1776 | -58.621399 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd3bab52-b39b-3526-ab22-de45a7fa2975 | -4.3197 | -54.886398 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2720ef72-f4bf-34ef-b0d8-18195817df44 | 3.5178 | -51.243301 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 51befeb1-f25f-3f34-b6a1-523025b0abf1 | -2.8456 | -54.110699 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d327477-638f-32f4-9fde-04a0e7dfde7e | -12.5258 | -49.675598 | 2026-10-09 00:06:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b916d2ee-f70b-3571-bf67-9131d4d5c64a | -7.5811 | -47.034901 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23365d03-533a-3459-83e6-d859a0979471 | -13.175 | -54.323502 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bec23a3-47c7-3ad3-a55c-d8b253e8ceae | 3.5162 | -51.250099 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a01ca235-ac39-3aee-87df-b73cdaf61f02 | -7.3934 | -44.756802 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 23170bee-bf3a-3fd3-8633-6e11f73ebd7f | -5.2751 | -47.912601 | 2026-10-09 00:06:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a04a48f-fb12-3288-8b01-5ecee94916fe | -13.1555 | -54.3274 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a09390b9-f489-38bc-9331-4c1eeb946e6d | -6.6659 | -55.094898 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7629a4-fb68-347d-8a99-7f5c373c9c1b | -3.5775 | -54.6805 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b78e235-c323-3746-ac04-e5a1ac7236bd | -12.0062 | -43.479198 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e30bde27-c47b-3b9c-9d52-d4fc105aa218 | -4.5463 | -47.025299 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1212ddd-43bc-316b-86c4-175bb45bb17e | -11.7696 | -43.5275 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17aa35df-4257-3e67-aa1d-391d83e88a54 | -17.370899 | -48.1805 | 2026-10-09 00:06:00 | METOP-B | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dc5d663d-9361-3fcd-9f73-3660ae72c739 | -4.3249 | -55.004002 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d42398f2-0252-3222-9192-a59203dcd246 | -7.2163 | -55.139 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 429880cf-5c9f-355b-bcde-53fd0823a6b9 | -5.7607 | -43.866199 | 2026-10-09 00:06:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03d87c46-76e3-31c0-b197-579a189445df | -6.8769 | -43.704498 | 2026-10-09 00:06:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4533e2-7189-36cb-86e2-efbd304a4d7f | -5.0921 | -46.214699 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92667097-5ec6-30a1-a5d0-c9332ca128a1 | -10.2558 | -44.637001 | 2026-10-09 00:06:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6f361253-fc47-3033-9aad-a832915252ba | -5.0947 | -56.1926 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb32dbc-15a6-34b2-bcaa-80890b402487 | -5.9878 | -40.945801 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e3b5c01d-ef6d-3e42-b5fb-fe316b9cedfb | -4.9027 | -48.770199 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b504fb2-6224-3c31-8299-c87cdb09d88d | -2.8303 | -54.134102 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15eecf41-9e77-3936-bdfd-604154542494 | -5.4999 | -42.8521 | 2026-10-09 00:06:00 | METOP-B | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e781d875-638e-33d0-91c2-ce013b7fbcad | -6.7192 | -55.057499 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933a379b-4851-3f4b-a429-55a83533ec7c | -12.5411 | -46.528301 | 2026-10-09 00:06:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe9b937b-122b-3444-828e-2a37025db5b8 | -3.5532 | -54.663502 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5b7d280-8441-3a2b-a063-76cb52cb275c | -9.1043 | -48.801498 | 2026-10-09 00:06:00 | METOP-B | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a8e31676-6099-38cb-88e2-5d07abe60b85 | -3.2981 | -53.697399 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b99249b7-a87b-35b3-8fb9-5c2f5a0b3b60 | -10.3711 | -45.129398 | 2026-10-09 00:06:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 654bcb5f-b418-3c75-876a-59b06a8b5772 | -2.9381 | -54.1106 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbda1811-f4cb-371b-8610-8069837135b9 | -9.2918 | -47.435699 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc0a9a67-a828-3984-bd24-8d501f3cf5fb | -8.7287 | -45.125801 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25d61f66-92d6-37ab-b562-b6ca1d0e4256 | -12.2258 | -57.101799 | 2026-10-09 00:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa159a68-8cc9-3e34-aa6b-f73d0b2faa17 | -5.2638 | -50.144001 | 2026-10-09 00:06:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03861c47-34d5-32b1-ad22-395cc96a6b6d | -3.3026 | -54.041401 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18690ee9-924b-321d-b258-944c070f86ca | -18.7834 | -46.472 | 2026-10-09 00:06:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 80337c04-da6e-3a71-99c2-1b847e8189fc | -2.996 | -54.047901 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f349e53-98b0-39a1-b931-a4e5dca40a5f | -1.4588 | -54.753101 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 511042bf-88dc-3826-bf39-be684956c986 | -8.9927 | -45.905499 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3eeb4298-004f-3d8f-8111-5ca5e5fc082a | -6.471 | -55.473202 | 2026-10-09 00:06:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 387c1747-5cd2-3645-b0db-241857945b88 | -4.5365 | -47.027599 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13c882ab-5b9f-3372-ba22-173d1e130fd6 | -3.0032 | -54.126701 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3cafb70-bbe6-3c6e-84c7-4b8b01dd01c4 | -12.0091 | -43.448399 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31bec418-a9e5-3995-9c3e-b62bf8d668ed | -2.7456 | -54.122501 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e61cb3-5874-3948-bac8-2f583ab67f8d | -13.2098 | -54.345798 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acae3c35-5ecc-30a7-b4e9-0f1b9a793d6d | -14.2621 | -52.777901 | 2026-10-09 00:06:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 719a00fa-53bd-3e2f-bc70-1568c43556b8 | -4.7322 | -55.650902 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)

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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1b57f5e-9b4b-34bf-a447-979eb896b91a | -8.22287 | -49.49186 | 2025-09-16 04:51:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aa909fd-1aa1-3b37-983a-ade65280e23d | -11.11063 | -45.35242 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7c4b0da-6435-3137-9984-dee411fe2255 | -12.80706 | -47.24335 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d70fa418-c5f2-3a51-9a23-cb8306e3511a | -10.71384 | -46.48398 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 87857435-050d-372d-9d58-42e41db280e8 | -10.17257 | -46.1426 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c64e8338-d3a8-3f8d-a669-3fac0595d5d2 | -8.57714 | -46.36298 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6c28d27c-56b2-3125-89f4-9065353ecce4 | -9.09458 | -44.86804 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f305a4a9-3b86-3e97-8232-205339a994c9 | -8.43143 | -55.63907 | 2025-09-16 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f04f1e4b-4580-3a08-b935-c9e6ae604d07 | -8.84824 | -62.93453 | 2025-09-16 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 841ec2b5-fd80-34df-ab43-275bbe3e02d1 | -14.60589 | -46.38854 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ea9e3ea-8863-3c09-9a81-bbb7d0594a2b | -9.05169 | -47.0162 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ebec9c-ed74-32c2-a69a-88f303230f68 | -12.17751 | -44.10246 | 2025-09-16 04:51:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3155c369-f391-3b95-bb99-ca2607c5f69a | -8.67862 | -49.93599 | 2025-09-16 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 125216ea-00c1-365d-9c26-cfcb8dffdfa9 | -14.66276 | -52.09781 | 2025-09-16 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 273edc07-3379-3894-84fb-991245171c6c | -11.70294 | -46.87256 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a9ef0c2-b4e9-3608-b2b7-31cb7087aef1 | -9.46471 | -48.58533 | 2025-09-16 04:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 298f5b4b-7096-35c6-977d-70e769b36bbe | -13.75654 | -48.76644 | 2025-09-16 04:51:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a496037-885f-3848-b302-ed41e599895d | -12.11537 | -44.84358 | 2025-09-16 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31bd19a7-3e1c-3784-99e9-b6eba324470e | -8.58869 | -46.34603 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6c4c0a8d-95a1-375c-b9d8-20ad45c18ec1 | -11.70354 | -46.86815 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a8ee2f83-f417-3f2f-ba08-ce647bee7b24 | -12.79621 | -47.25579 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b6d4b07-3bb6-3022-a7f2-4347124330ae | -12.64741 | -47.95944 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bbb6e61-89de-3dca-8e95-3700ce40b114 | -8.97425 | -45.0409 | 2025-09-16 04:51:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55b3c1e5-fb54-3888-976c-f032b26d5274 | -14.47594 | -46.35672 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb1041fa-e500-35d1-9748-e3a4dfe3c900 | -14.87772 | -51.633 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df3964d9-d0a8-3e28-b957-77b8cbb5f34b | -13.06396 | -50.08229 | 2025-09-16 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06148c69-6a42-3fb2-b238-d7b0ad33a613 | -9.10079 | -44.85995 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 24274adf-3a1b-3b45-82d6-8cf9f3b5b59b | -10.60346 | -55.39495 | 2025-09-16 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a504197-fa7e-34df-90d2-33e4612ba3da | -11.69844 | -46.87147 | 2025-09-16 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8183687-81fb-320e-80cd-2010872fa3f2 | -12.76149 | -47.96127 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8b24d4a-fae7-3034-b968-c9766ec7be97 | -9.6807 | -48.83629 | 2025-09-16 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b39a278-c3cc-37a3-8ab8-a449cd0cc9de | -14.81968 | -51.66354 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3181726-8c14-342c-81ed-1051e7ba3d5a | -8.96912 | -44.19106 | 2025-09-16 04:51:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 110c4774-9215-3bb0-8d2f-63a905581028 | -14.80365 | -51.67374 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6196142b-fe1a-3ec2-a5da-12c80217883f | -11.12015 | -45.31849 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e31d89e5-5a91-337c-bde7-e810c4c86ea3 | -8.90065 | -46.15208 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2563cd60-3533-34cd-9ec0-24dc002a7eb2 | -10.71789 | -46.48893 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 0436f69f-17df-3016-bfb1-37e3d4a603f4 | -11.1214 | -45.34824 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1380caac-421b-31d9-8de0-5b7e38d14cca | -14.9085 | -51.67156 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 224edf8f-7164-349b-873a-bedc07142c80 | -12.66996 | -47.94081 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffbf8240-caed-3a9c-a54f-40ec87fb9406 | -9.63724 | -58.94623 | 2025-09-16 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 432727df-9eb2-3ffc-876e-f504896936d7 | -9.09572 | -44.85943 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cbe6e7b8-055d-3e9d-959d-d33273922986 | -12.64574 | -47.95831 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89b56bd8-a449-374e-a9ee-d199bee0cfa3 | -11.11712 | -45.34179 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1eb274f-b173-385b-98f1-077d47eab049 | -11.45796 | -46.9236 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d40c8fe-db44-3375-803e-6525a7d7703b | -9.08824 | -44.84665 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7908721-edf8-31bc-bdd2-c75ea7a9e357 | -12.96991 | -47.96334 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 364973f5-53e1-398a-a9f5-d35d624aed49 | -10.78259 | -49.13564 | 2025-09-16 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3ff92c5-314e-30bc-89f6-2dab838655d3 | -14.82323 | -51.66409 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c23d0feb-13d3-32a2-bc05-03b86955083d | -9.06295 | -47.03079 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 27f95029-ff1b-3431-ae0b-867868fc30fe | -8.89057 | -46.19018 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f772c6d1-7c9b-3529-80d2-934ef1e2406f | -12.4416 | -44.74857 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 955a21ad-fc47-3993-9646-89b18163a52b | -14.91206 | -51.6721 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2727d56c-0b78-382b-9a2d-00755d3cb789 | -9.20967 | -44.5117 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a95a57f-dd57-321d-8bbd-5abbf73bb004 | -9.04657 | -44.85038 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53472e8f-5298-3905-ba05-d9a9249d29fe | -11.43726 | -46.94023 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b78c16c-cdbc-3227-99b1-c2513ed09288 | -12.61341 | -47.98396 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94187eab-0996-376c-9cf2-82dd90a7d1c2 | -15.07562 | -52.47915 | 2025-09-16 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8240ee4a-c5fc-32c4-82df-3f8960653eaf | -12.11882 | -44.81563 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51d8a061-95fb-3bf5-9724-86fa35d3ef25 | -9.09884 | -44.8445 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e862e61-a9d6-36f0-9a11-e40bf8bbe34a | -11.43851 | -46.93093 | 2025-09-16 04:51:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e573183b-c561-39c0-96c3-7877da1b7288 | -12.27763 | -53.92191 | 2025-09-16 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac708166-a069-3162-ab78-43242e9d9ff3 | -8.9099 | -46.15306 | 2025-09-16 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f257a61b-56ea-3457-ad1e-e4a9f9e76050 | -13.21246 | -47.28572 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2be0879e-bc9c-3a9c-878b-e541c4430fc4 | -9.63306 | -58.94561 | 2025-09-16 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17eae1a8-3f90-3e5e-8a6f-0d0f49da5f72 | -8.67193 | -46.37709 | 2025-09-16 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22fd1fca-23de-3ee6-b715-a3a073855c0d | -12.61932 | -45.74073 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 636ac434-4fc6-3f97-a940-09f139dd31de | -10.07563 | -58.61806 | 2025-09-16 04:51:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d09b5615-7baf-3078-a336-07c087e138c3 | -14.60165 | -46.38238 | 2025-09-16 04:51:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e544537b-0e19-34ee-9def-5038113c017f | -10.71475 | -46.51263 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52ed56a9-4e9f-3bac-bd78-769a984e2de5 | -13.02063 | -47.95998 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59b72a1c-9262-3c08-87a0-edac6d09dec1 | -12.81858 | -47.22593 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dcd1e4fb-7242-3b32-97d7-4f5dcdc202ca | -11.12677 | -45.30703 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1146a420-2168-39e8-b4b5-1515028442ad | -10.36686 | -61.26183 | 2025-09-16 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b17f220-0f6b-3cc4-a751-0cbf527b325a | -10.7241 | -44.74781 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f271c41-9c71-3e6a-8637-c6d786cc9c65 | -12.6624 | -47.72167 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e062dffd-36db-3262-a060-c1e96d4c808f | -11.27594 | -50.79298 | 2025-09-16 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 937dfed5-4ab4-3a16-a8a5-9659028bf455 | -12.66925 | -48.01217 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4eee7333-b744-37e2-8b1a-d478a35959b3 | -9.09689 | -44.85855 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef5b9fc5-05bd-3f23-8cf4-ebacc67400dd | -11.13258 | -45.341 | 2025-09-16 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57c0a326-c49a-3e18-b83e-a6036d39e9de | -12.64601 | -48.00117 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eef39f5-d86a-318f-a937-dd3736d68847 | -14.83265 | -51.6684 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b4d56e61-b1ac-3f58-b85c-669fe6ad38a6 | -14.84152 | -51.6317 | 2025-09-16 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89b3889e-25a1-378b-9f00-9399e0880221 | -12.10708 | -44.82381 | 2025-09-16 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9720c2a4-0d39-30a7-a928-3207fe9f543f | -9.07065 | -50.30669 | 2025-09-16 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3deebe57-9b88-3fc7-8fd5-245e8c536a4c | -9.60521 | -57.74427 | 2025-09-16 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbae03a3-ab91-35f9-8ad9-22c22e66e141 | -8.60222 | -45.74281 | 2025-09-16 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 49fab8f6-d77d-30b9-920c-31f3637bef40 | -11.46646 | -48.69762 | 2025-09-16 04:51:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48198365-2a1b-3ee3-b9a4-86d8ea0355d4 | -12.62501 | -45.77684 | 2025-09-16 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d82d811e-8191-3c66-ba37-fa74731ccd9d | -10.65225 | -46.45772 | 2025-09-16 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c27c67e-2d21-3d89-86cd-087d83d80513 | -14.50844 | -47.32595 | 2025-09-16 04:51:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66ed69b2-3cb4-3a04-ac31-79cd34282705 | -9.0532 | -44.83944 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e2430eb-0049-3c9d-a260-0eb68856837b | -10.71268 | -44.74598 | 2025-09-16 04:51:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3992285a-dde1-39f1-aacf-4c7ee0d4d914 | -9.09529 | -44.87004 | 2025-09-16 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eba511ea-e5a2-3c6e-bd30-7762a16e3685 | -13.01632 | -47.95928 | 2025-09-16 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba6e711c-ead7-3da9-a4df-cc3b6d0e2d60 | -13.20965 | -47.30732 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 32352c71-9d35-3cd4-bec3-3138809e0572 | -8.12602 | -50.16935 | 2025-09-16 04:51:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcc78bde-4cd7-369b-94e4-ac5e50c1e28b | -12.8055 | -47.18516 | 2025-09-16 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d350d4c-16a6-3ba8-a08d-0f880f34e18c | -13.8792 | -44.85282 | 2025-09-16 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd69d939-f08a-306b-8e3b-fb579f623d23 | -12.05904 | -46.55126 | 2025-09-16 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README72.md)

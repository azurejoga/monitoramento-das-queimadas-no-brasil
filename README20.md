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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 373f1b63-c41e-3759-b67e-a980d31448cf | -2.96143 | -49.26508 | 2026-08-11 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 4eb54731-9477-3b96-8487-480b5ede0ee8 | -1.78578 | -55.52772 | 2026-08-11 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c16c2f-1fa1-32c4-9d46-98edbb5bea3b | -4.27124 | -48.18745 | 2026-08-11 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c2aac8cf-a6e1-3338-82f6-63d19de481ed | -2.74272 | -54.59362 | 2026-08-11 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 611b07ce-b68e-304a-9758-a271c0525fbc | -2.45325 | -54.73672 | 2026-08-11 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 479beba6-9e08-3952-a3ec-e319e9d8822b | -5.31748 | -43.55993 | 2026-08-11 05:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df09eaa1-7432-3bd9-9cb8-37a5ec07bb6b | -4.39423 | -50.96371 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1ba3a24-252f-3ddc-a0a4-118ac136fff6 | -3.85756 | -54.08056 | 2026-08-11 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 718ba808-870c-3a3c-acc7-ce0575407779 | -4.45339 | -47.91448 | 2026-08-11 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3ddf8388-e0b1-3ef9-87dd-5a10f9d1533c | -4.45771 | -47.91513 | 2026-08-11 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 307be8b8-b883-3979-941e-c846d3489e7e | -4.39872 | -54.78585 | 2026-08-11 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e51ffb6-ea89-356b-9425-7185d8bade84 | -4.40358 | -50.96386 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5931034-e615-32d3-919a-0329d5e73e46 | -0.86784 | -47.92923 | 2026-08-11 05:08:00 | NPP-375D | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a59cf678-ab09-3d1d-9cd5-ecead7addf18 | -4.39937 | -50.96741 | 2026-08-11 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5a49a52-2e8b-32c1-b4b0-27e57fbcb6b7 | -6.01301 | -47.40126 | 2026-08-11 05:08:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f6cb871-0079-3b3d-b222-52e503d677f3 | -8.9598 | -60.555 | 2026-08-11 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 76529dfc-5483-3af6-b693-bcf48c059c4f | -9.3909 | -47.4656 | 2026-08-11 05:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f440eb5c-760c-3b51-a8c2-057eeba99946 | -8.9414 | -60.5367 | 2026-08-11 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3459794e-4677-38a8-bd1a-5f397747810b | -11.4701 | -46.682 | 2026-08-11 05:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 85a9cab8-85cc-3a9e-bb64-c5a596ce4d39 | -8.96 | -60.5358 | 2026-08-11 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d5c299c7-4d0c-3daa-9deb-06f1b7a5ce5c | -9.3906 | -47.4878 | 2026-08-11 05:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 48131d97-9904-333e-aee7-de4850ef445d | -9.4098 | -47.4636 | 2026-08-11 05:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 77e27b56-1567-3255-ae5e-954c34b62522 | -4.2635 | -48.1799 | 2026-08-11 05:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ddf6b6d0-7793-32ed-9847-f114519a892d | -8.9412 | -60.5559 | 2026-08-11 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 2387ccf1-8aa8-3419-b7d2-21a86ff6a3f5 | -13.5696 | -46.2813 | 2026-08-11 05:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2989623e-2110-356d-97f1-3bdf5739dba1 | -9.3903 | -47.5099 | 2026-08-11 05:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 410cad0c-b1ea-37d4-9c2b-9aea52d94dfd | -13.60409 | -46.31886 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb29c212-48e5-38ee-b38a-a577bdaff84b | -11.95525 | -46.33323 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82979d24-4f00-3d30-9529-aac803a891b4 | -11.2331 | -54.84695 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1b7e77e-1e47-3597-92ec-3ac59b0d7651 | -9.38773 | -47.48508 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f940c0dc-bc8d-311e-ba16-37c478422a76 | -11.46234 | -46.65696 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d3a9ddf-cebe-3a57-8dd9-f00edae65895 | -11.46829 | -46.65502 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908a5838-38fa-3e3e-9c4b-d613f60d8a13 | -8.90333 | -60.58332 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afb96bec-0f4e-31b5-9cc8-6b8f2d13c4d1 | -7.4122 | -59.99701 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f4a36c9-f85b-35d3-8070-3ea49ee1e4f8 | -8.23553 | -46.24227 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7fc9bf5-7fa7-3fd9-890f-7e71ef21658b | -10.73196 | -50.4355 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38629a5d-f29f-32bc-9e24-b8c9d487109f | -8.89425 | -60.5857 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bec18e2-ce90-3fb7-8062-2dd57b395c98 | -9.47317 | -60.51943 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae575bc5-c9e9-30da-95d9-d4a538e2b9ff | -11.88511 | -46.80971 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83682984-cf42-318c-862b-a3772248a83f | -7.71595 | -46.21985 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 759be060-dd7f-32e9-bfb2-0e47f97b0089 | -8.89884 | -60.58307 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6de955a-5147-382d-8378-ff7a1b1431fd | -7.40679 | -60.0037 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c460305e-f0f5-3cf8-a471-4bf2910f1fb7 | -11.975 | -46.35014 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba6a4fdc-af6b-3158-983b-647823da75fa | -11.22865 | -54.83173 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 625fb361-2062-3711-b5c4-8e693b754400 | -10.11262 | -46.19504 | 2026-08-11 05:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4b6dfab-a5b0-3e19-b5d7-c869606e1456 | -11.46459 | -44.5723 | 2026-08-11 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4b67922-86fc-33a9-96d6-a7c52167b10b | -9.38076 | -47.50019 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dbbc0b99-a278-374b-960d-f4ad1685cd7d | -9.47051 | -60.53454 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05b2bb6b-abe9-3b8c-972a-f1de634023f3 | -12.23833 | -47.30517 | 2026-08-11 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 014f39d3-7d2b-39a7-92b0-75f04ad88664 | -13.58093 | -46.27898 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 244c88b7-dc3f-3e72-9c95-00f66a189820 | -10.2218 | -45.83903 | 2026-08-11 05:10:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5d25d34-a7a3-32ad-8900-98bb4d7d95c9 | -13.56395 | -46.28051 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0fd4ca31-93a1-320c-97f8-b9f2af5d5ab2 | -13.56438 | -46.2769 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5ea413e-9728-3f53-b71d-911e4ec5f96a | -13.55457 | -46.31239 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5273fd6a-2d51-3d85-8c4a-840a22459fe6 | -12.46429 | -45.3371 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccab2131-e638-3c4f-929b-d2c261714e98 | -8.29588 | -46.4079 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4d180f30-cd4e-356f-8fc4-51c9daad6046 | -9.3741 | -57.36317 | 2026-08-11 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72a1fc81-0724-35a4-81ad-4df2844617b0 | -8.29921 | -46.40918 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac88b781-7de1-34ec-b57c-f17e4b42068e | -8.89465 | -60.58231 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4adb35dc-e661-34c9-be74-bfaeb800ba3c | -9.47251 | -60.52319 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 370a8279-ae36-336a-a088-e98bd1d84834 | -8.94268 | -60.50683 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a54b12ac-533f-3996-be08-087407bccae6 | -10.93572 | -57.11861 | 2026-08-11 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 043b7529-d34f-3162-9637-c5f83d9beeca | -11.92245 | -55.90116 | 2026-08-11 05:10:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b026cbc-8224-3385-9a5a-eefcdfdc5281 | -10.72796 | -50.4349 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2283e4d6-f50b-39e7-853c-87a766b67437 | -13.56989 | -46.27769 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2da998b4-ce6a-3558-affc-3375382ec172 | -12.4624 | -45.30748 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 81f7bd13-5d69-3f7a-8641-ee748f5082f0 | -13.56266 | -46.29137 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f0802e45-1147-308b-9214-5788d2f1f811 | -11.47792 | -46.62071 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4df7bd5a-c291-3db7-80d7-62d5a5a0e120 | -8.55153 | -45.34816 | 2026-08-11 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40d6f5d5-002f-319b-b6ab-6d95d668f8a4 | -10.4159 | -46.64331 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 057003f3-3145-3b14-9616-799493c6317b | -11.23199 | -54.83226 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0a2c703-6ed7-3011-910e-8866ac7e4daa | -9.4697 | -60.51494 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2d24e0d-6bb2-3175-b5e0-f2fe302e0663 | -13.56816 | -46.29215 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5bcbd8ac-3105-33ce-a92f-97b4c35cd8cb | -10.41059 | -46.68421 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 268af893-b325-3f0c-8388-611e83057cb8 | -12.11758 | -47.18886 | 2026-08-11 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f80864ae-87d3-3577-8ded-28d0db3176c1 | -8.94818 | -60.49994 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6efabc11-4acc-3857-b52a-3296e014eb52 | -11.19924 | -54.84514 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5ce1090-c4e4-33c4-8df7-ceec474a7d3d | -11.23421 | -54.83987 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46064857-7cea-3e1b-82d0-29cfc56f5c7e | -11.19092 | -54.85468 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 519f0ec9-cca2-3ffb-ba5a-951db5062964 | -11.48709 | -54.60656 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 262eb3af-34d5-3494-a1fe-cff599f245f9 | -9.47331 | -60.54289 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cff9635-d394-3ccd-8ce1-1915a689bbf1 | -11.22921 | -54.84996 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51563aae-6659-3b5f-8529-ad982b4cb075 | -8.30241 | -46.38532 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ce3307-2002-3174-9ccf-7a5632b53a6a | -11.96902 | -46.3543 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9eceb5f-0b03-3386-9672-785ac63d7c2c | -11.58969 | -54.48666 | 2026-08-11 05:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada34f91-038d-393b-b0db-c8d146e40958 | -9.39396 | -47.47543 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f68a3914-771c-31d7-9ce8-b804a0bbcc19 | -9.38221 | -47.48971 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| c0a7c99c-aa2d-3619-88eb-c518a457d610 | -11.19536 | -54.84814 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc1c2f89-ada8-3986-85b1-949d944be6cd | -11.22199 | -54.83066 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52abe074-5a02-3fdb-afdc-bbc6de886497 | -8.36845 | -46.39564 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63575691-194a-35e8-b6fc-afc72ce6107f | -7.65714 | -44.38783 | 2026-08-11 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67f7771f-ed8c-3238-a98c-e238225115a5 | -6.70918 | -58.94748 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 395ad76e-8f0c-3c5b-8729-ea1b56a29daf | -10.41574 | -46.68489 | 2026-08-11 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ef9d559-f656-3b69-ae4e-bc5c046558fb | -8.94335 | -60.50302 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f764aac-9b72-3cdb-b4ec-a3e75c0386bf | -8.95236 | -60.50066 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea20b2c2-44eb-3202-8547-9d6c39abfcfd | -10.497 | -50.30605 | 2026-08-11 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d353830-b97e-3ae3-90c4-fa2bfad90650 | -10.8614 | -50.24864 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a7a36cd-4107-33ce-ac92-9e2a1454c868 | -11.45958 | -46.68217 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fafed8e9-dc3c-31ff-b08c-e6d1ce5f8809 | -11.26312 | -44.8762 | 2026-08-11 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72b78abd-d902-318b-945f-84a98e9a2f32 | -11.64516 | -51.64924 | 2026-08-11 05:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README21.md)

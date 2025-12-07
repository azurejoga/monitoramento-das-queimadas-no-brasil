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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ee202dd-9041-3ea4-8f2b-66d4aefd9eb8 | -3.13194 | -52.84816 | 2025-12-07 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4391a4b-82be-31b2-a470-32ffe22f6e1a | -2.69202 | -54.62952 | 2025-12-07 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb1bf77-0a4b-34d5-932c-180422e8be0e | -2.77622 | -54.52684 | 2025-12-07 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c9f70c3-47b7-3634-ae7c-e8af69dc9221 | -1.58859 | -53.81238 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7801ee0d-9d9a-3f16-9ee9-33d7dd11cc0d | -1.70572 | -53.67242 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d4262f4-2863-3f9d-ab84-f2dfa4ba136c | -5.1383 | -60.38529 | 2025-12-07 05:03:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 586fcf31-3f0e-3b97-af4a-45154ad46887 | -2.1801 | -53.55385 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd8db6b8-000a-3550-b1a1-d23f5ace0057 | -1.30877 | -53.49227 | 2025-12-07 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2724235d-1b24-35e8-b57e-467c424de243 | -4.25918 | -48.83805 | 2025-12-07 05:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bd0b0ea-bf89-309d-877a-8c4555216ac4 | -1.61667 | -54.72111 | 2025-12-07 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ab6b183-2c89-3e64-9b01-92834e270c7a | -1.46561 | -55.09839 | 2025-12-07 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1000b68d-9514-3251-a443-90e5b56139cc | -2.17954 | -53.5574 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca385210-f17a-37fe-b92f-55e2c655c562 | -2.17619 | -53.55688 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f9c57c0c-1b38-3cc8-aeed-68296cb4564d | -2.38589 | -56.05861 | 2025-12-07 05:03:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84ada738-cf8c-3f8e-a2a8-0ff849503db9 | -1.31211 | -53.49279 | 2025-12-07 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57bf06c9-6c35-395d-87bd-be71a9ed85f7 | -2.05748 | -53.12342 | 2025-12-07 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47095d5d-afa2-3cd6-b375-39b906b0ab24 | -10.55083 | -59.4143 | 2025-12-07 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6f9b3c8-a562-35f4-83a0-e39e0a28424e | -10.54665 | -59.41769 | 2025-12-07 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a451b37-376b-3d31-834d-80637446d9c0 | -10.55017 | -59.41826 | 2025-12-07 05:05:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a15b35a-4909-38a2-ad2b-ee89bea29c23 | -10.99281 | -54.25377 | 2025-12-07 05:05:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8484f9fc-c851-3ac3-8699-52a2e9d0bbd8 | -20.91918 | -56.37573 | 2025-12-07 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 62c578d6-3cf3-399b-8a77-5d1ece311886 | -23.2979 | -47.09219 | 2025-12-07 05:08:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1037cbd3-edd6-37cf-97dc-5c90a8375011 | -22.45348 | -49.81695 | 2025-12-07 05:08:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c10a5578-3322-3d1f-84c6-be91ffd27633 | -23.29365 | -47.09337 | 2025-12-07 05:08:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 256872f5-790f-303b-bcf1-447898cde886 | -20.20016 | -52.92397 | 2025-12-07 05:08:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e70e12c-f8ff-39ea-9dd1-d9a6b566b889 | -20.19966 | -52.9281 | 2025-12-07 05:08:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eef47665-ccc9-344a-8fe9-9c2b7954fed3 | -20.91976 | -56.37148 | 2025-12-07 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d610d163-09da-384a-96cf-80e296f4f1d6 | -19.44043 | -54.12992 | 2025-12-07 05:08:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4a839b6-2f31-3459-92be-f9a449ad45af | -23.29404 | -47.08791 | 2025-12-07 05:08:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 014178dc-38cc-3135-b573-5def8c04dc49 | -20.72684 | -47.35224 | 2025-12-07 05:08:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11092f85-2cb0-3416-acc9-369f10ee3214 | -20.72071 | -47.35177 | 2025-12-07 05:08:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baf7b073-9b00-3f71-85f3-70ffa710a916 | -23.29149 | -47.09193 | 2025-12-07 05:08:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cc408c41-5a08-3f86-9fa4-c13d1e13dc57 | -20.91859 | -56.37997 | 2025-12-07 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 35f342e2-dad0-35c1-b2e9-610a439937bf | -20.2044 | -52.92464 | 2025-12-07 05:08:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9891f9d9-0227-3b46-b2af-af479d7135e8 | -28.24454 | -54.00671 | 2025-12-07 05:10:00 | NOAA-21 | CATUÍPE | RIO GRANDE DO SUL | Brasil | 4305009 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 14840918-280f-379b-b9b0-f3820cb89b51 | -29.08492 | -50.62545 | 2025-12-07 05:10:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b01aefb4-beb5-3bc9-8a9a-cec4521dfeeb | -26.21022 | -51.56519 | 2025-12-07 05:10:00 | NOAA-21 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a5d3fc4c-abd5-3e55-927c-6998e6fbc0a4 | -26.21085 | -51.55825 | 2025-12-07 05:10:00 | NOAA-21 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0caa3d03-319d-313b-b73d-e4cbc65e2efa | -30.72534 | -52.3609 | 2025-12-07 05:10:00 | NOAA-21 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| bd6cb40d-a9d8-3da3-8cd6-141b5864a9ad | -28.90337 | -51.04756 | 2025-12-07 05:10:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 70dfbe70-be72-370e-b56a-b43672f35fd4 | -29.08462 | -50.62942 | 2025-12-07 05:10:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 03dff048-1997-3649-bd46-0ce0673d0ee7 | -26.08182 | -51.58532 | 2025-12-07 05:10:00 | NOAA-21 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9b6635b-56e7-39e8-ba09-85f1867cb7dc | 3.9837 | -51.67067 | 2025-12-07 05:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d73b1be1-eb2f-3d79-b0a3-23fc5c49f523 | 3.97964 | -51.67722 | 2025-12-07 05:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b80c3a5-aa15-3028-b1d7-3aa83fffb12a | 3.98464 | -51.67634 | 2025-12-07 05:29:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef79932-88fe-3b04-9941-39092761a2ad | 3.44624 | -51.24778 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46d89a69-eea1-3dfe-9695-89b3ddb49dd7 | 1.59017 | -55.96771 | 2025-12-07 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8387df3e-20ad-3ab5-b263-3b43f194e20e | 2.50798 | -61.02896 | 2025-12-07 05:31:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd5f4ba1-197c-3ce1-8fb5-c56cf3e771c2 | 2.00396 | -55.6799 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15fd8a1b-c8ff-3344-84eb-f3e8c6dcfd8c | 3.45038 | -51.24063 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43918ec8-e82d-3788-9d9f-05be481dbc3c | 3.40582 | -51.26273 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e25e4fd8-eefe-3cb8-93e9-af7c86d6a3df | 1.97072 | -55.69164 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dfd9881-e63d-3619-87be-3a272351effd | 2.0087 | -55.68425 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b9994e2-fac8-3fc0-9d5b-d7b7f9d5e220 | 3.45091 | -51.24377 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ef1f41-c73b-392e-87c0-87adae6c3f6d | 3.45144 | -51.2469 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d44694-46fd-3544-9a7f-5de9fc038c59 | -1.46755 | -55.09974 | 2025-12-07 05:31:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513793a6-8479-3a7c-b174-ef57318d4cbe | 3.41038 | -51.25704 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d465b9ec-5393-39b7-9f66-58ac7dd034d4 | 3.40626 | -51.26418 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6d9d8578-cde5-3523-a1ad-02ea6163ac28 | -2.1785 | -53.55997 | 2025-12-07 05:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d3e52e0-cdb6-3fd2-ad26-b50232f129ff | 1.9961 | -55.68121 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31d3400c-c27b-3cd1-bb40-c2c5dde63a05 | 3.40106 | -51.26505 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 403ecd70-9e2d-3e30-bff6-e4df01e957c6 | 3.40633 | -51.26587 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d284b23a-adfa-34e3-be48-633a74bc2940 | 3.41092 | -51.26017 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9547be7-3132-341c-aecd-ce4f249ae254 | 1.32608 | -50.95181 | 2025-12-07 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab1a3e4-9bd9-31cd-a472-01eeeb970e8a | 1.33156 | -50.95088 | 2025-12-07 05:31:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9df3169a-b45e-35ad-9671-18015de7de71 | 1.97468 | -55.69117 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba8aa14-8709-32b6-9dce-d789b7d45242 | 3.41102 | -51.26185 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0d27dc7-fd57-3ffb-bada-9abdc403615a | -2.1793 | -53.55471 | 2025-12-07 05:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9211b61e-e74e-393a-b5c3-f9edb76f5b27 | 3.40062 | -51.26362 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2946ada-2212-38ce-8bd2-7bd757f3b156 | 3.40531 | -51.2596 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4887273-680b-3504-a6b5-692f56712165 | 3.4016 | -51.26818 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1123f2e8-9519-3962-accd-19338a13dfed | 3.45559 | -51.23975 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b761cb8-e7fa-3117-87f6-f914dab7c337 | 3.41051 | -51.25872 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a38bcdbe-0684-3915-a82f-a2ffa7901f43 | 1.96757 | -55.69724 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 06bd2dfc-200d-31f9-8703-801a211a16fb | 2.0064 | -55.69495 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb1565a2-88a0-39a8-a2f5-175c0fb7b2f6 | 3.44677 | -51.25092 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b209ba8-2de4-37bc-8e11-9aa761e068f2 | 0.45642 | -60.42728 | 2025-12-07 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a69b2f8a-fb11-3c4d-84f3-d486ee530adb | 3.40572 | -51.26105 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e80947f-0581-3afa-a753-400d09901054 | 3.42078 | -51.2553 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e7eb840-a2bc-3b3e-9869-23a85662de68 | 3.33526 | -51.31963 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db229a8f-f3b2-3f98-936a-b4c9cce80e01 | 3.33473 | -51.31653 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 179282b7-2897-3387-8bee-cb3e18c42afe | -1.58827 | -53.81126 | 2025-12-07 05:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc7b75c3-e0f6-31d0-acc4-598cef04fa48 | 1.97407 | -55.69467 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d5657b0-2d2e-3b69-b232-7ac97f525a0c | -1.1753 | -54.19173 | 2025-12-07 05:31:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43acca97-05e7-33b2-866f-75b7304b726e | 3.41558 | -51.25617 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9f7d8ab-054c-3f79-9ce0-440df0b7f772 | 1.58995 | -55.96589 | 2025-12-07 05:31:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04f7f75c-13f4-3d7e-965d-25c54575d059 | 2.7166 | -60.73956 | 2025-12-07 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a396b0-8c0b-32b2-a693-3812cd4ab8f3 | 1.97011 | -55.69516 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 304de3bb-e6d2-33c4-ae51-15a0152c7a49 | 2.00478 | -55.68493 | 2025-12-07 05:31:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9901176a-5bad-3d27-bbec-7ce4ac84e623 | 3.40165 | -51.26989 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1fbbb51-abfb-308d-880e-3420f24db7a9 | 3.4473 | -51.25405 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 492ea6c6-1d8c-3d9a-b19a-33b084409c94 | 3.40114 | -51.26676 | 2025-12-07 05:31:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f755094-a273-3b29-b74c-159b6768c76d | -10.54749 | -59.41712 | 2025-12-07 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9035cc27-3e5f-31a3-a7b3-2dddc95494c1 | -5.13706 | -60.38563 | 2025-12-07 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f747da55-11fe-364e-a674-0c0881b3faa5 | -7.86507 | -61.49797 | 2025-12-07 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 402cb83c-bdda-336c-bbec-e922c38a468a | -10.54815 | -59.41258 | 2025-12-07 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9e2d2b9-eca1-36d8-8170-28d8561eb058 | -5.14046 | -60.38615 | 2025-12-07 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaebdcb0-b7f0-34c8-a73f-f7ca4079dd33 | -20.91505 | -56.378 | 2025-12-07 05:37:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e57dda8-7111-3cc3-aeb8-fcede41eea8f | -20.9147 | -56.38139 | 2025-12-07 05:37:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f54315b-7142-35d1-9a38-4cba1920789f | -20.92028 | -56.37867 | 2025-12-07 05:37:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README5.md)

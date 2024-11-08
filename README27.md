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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaf3491a-49b8-3e25-b1bc-5c3f7566c0b2 | -2.063 | -53.27534 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8f4f706-db7d-3ce9-bafe-25b1c4a34c3f | -3.38486 | -50.22187 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9f28a3c-2494-358f-9f94-86a2ef13a0ac | -2.94433 | -54.45423 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61226787-7f39-3821-a9e2-97fd7f2ac64b | -4.77426 | -48.66889 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f9a231d-3df5-3e6b-8b01-1325b188794a | -2.96267 | -53.8727 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d0523b3-86e3-3817-963a-91974e514f3a | -4.68341 | -46.40315 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 80633cbf-c412-3bfc-8735-7a22ce00777b | -1.07815 | -53.64469 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04bcc6f2-7a80-3f19-9e93-5a08694f9534 | -3.04906 | -53.27837 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42757620-edc0-35db-b184-caf78e5d68e9 | -1.15632 | -52.00409 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7242dc60-dd52-3ad2-bf81-d56dbab7a126 | -1.61745 | -52.25235 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac9f3fb-8198-3963-b73e-4223b7886105 | -3.25032 | -51.55459 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 463cff32-9c97-34cc-8dce-8f42718f66ef | -2.72282 | -51.71135 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b554402-dee4-3f7e-8f8e-6fb2d80f2119 | -1.21857 | -51.75701 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04ca6d82-b681-374e-9b5b-ac1c4b4ddf5e | -4.52283 | -45.67681 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0be5f17-02e1-3dcb-ada9-771da85fbca1 | -4.1386 | -46.90012 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6c254c3-a880-3b32-bd9b-b19f35a63042 | -0.9567 | -48.28407 | 2024-11-08 04:53:00 | NOAA-21 | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 420853a9-a396-3630-9fc7-0876353bda18 | -3.54083 | -47.37924 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9a24bda6-7d4c-3258-b3f1-2aba0ad91939 | -1.54414 | -51.85014 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8343a29a-4b6e-3c8e-ad5f-b143084f182f | -0.89768 | -51.76297 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64603aa3-b81e-36fe-89bb-66a147aba5ea | -3.56052 | -47.38247 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72b663ab-45ad-36d6-874c-20e5d5a6029e | -9.03497 | -61.99229 | 2024-11-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf600d7d-a882-3e10-9d73-b9c5030ae7b8 | -2.99111 | -53.89219 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfaaad09-bcb9-3efe-b3b8-2680fecee7e1 | -2.28441 | -53.81046 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df1f464f-1df0-3a38-b944-fd0eac5af19a | -3.72654 | -53.40209 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf8e7ae-ef5a-3d9d-960d-ebe7c17bf311 | -0.91042 | -51.65961 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fa747b5-3a8e-3b80-b496-653533b4e615 | -4.11945 | -46.91608 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30b42378-ab1c-3284-aa52-8d2bc6d06dce | -1.24444 | -51.76449 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b9928f1-e693-3c9d-a2d2-f1be3f03a3c3 | -1.12064 | -53.62074 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fcb3cb0-c84b-3a0d-ac2b-7ecf10b8657f | -1.4167 | -54.50434 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f6ba9ca-590f-3c02-9f6b-63b0e75c3163 | -2.98016 | -49.66109 | 2024-11-08 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b721d7a-f786-36e2-a3a3-012643a7e6db | -3.244 | -50.45328 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0f7a5c-876a-3352-bd6e-c7af6c07eb16 | -3.01823 | -53.43078 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeddaaa5-a926-3ae0-b098-7ba3b65328a1 | -3.80686 | -43.59704 | 2024-11-08 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1bc19202-67d4-3d1b-b2f4-1d824a1e0417 | -3.38277 | -46.10832 | 2024-11-08 04:53:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 966156d8-f095-3845-a94f-dd19195da316 | -1.34432 | -54.62206 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f29cbda2-169f-3493-ad9f-ca29d0680e2d | -2.0515 | -52.08738 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5025a20d-6953-3ab4-b174-d8c2672d579c | -6.08151 | -44.71615 | 2024-11-08 04:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab07cc63-68a2-32f7-9d5c-4578f960dc69 | -4.78656 | -48.67756 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37ec2503-2547-3002-b36f-bd83969bda26 | -3.33196 | -50.08543 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8895b8ad-4d48-3cc0-9eaa-d9f1e8da0a58 | -2.23212 | -53.67384 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33b4bc00-8427-30b2-9d1a-b37d6649b8c5 | -2.95293 | -53.28542 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37ccf048-7fcb-3871-887f-cbc49626e137 | -4.67711 | -46.44727 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03cf92ea-0562-36c8-b87a-5a1bc0b58a3b | -2.86371 | -50.32194 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bffb1c6-dfa5-39d8-ba12-73831769327f | -2.28216 | -53.80248 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1def9573-7ecb-37e9-bdc6-8ffd8a34081c | -2.81698 | -52.95643 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67582b16-3c18-3abc-9b0d-537c5e30f0df | -0.64425 | -52.3846 | 2024-11-08 04:53:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da86406e-b3d2-350d-a52e-c9a994c801bc | -1.18886 | -53.9013 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 409aece0-3292-381c-9575-41d9db187c4e | -2.45392 | -53.6923 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f0e1894-01cd-36e8-9bd8-4816a1ef79d7 | -2.05623 | -53.29643 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b13189de-5383-3db1-8341-f36769a7ae52 | -5.00017 | -49.91274 | 2024-11-08 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 319f14d5-ae21-3228-895d-a2ffbe79a0e2 | -1.14971 | -52.00307 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 29ed274b-1a32-3637-9b23-956faa3c715f | -3.03568 | -51.535 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55f26209-4898-35ad-8b2b-37e1056760e5 | -3.0429 | -53.27379 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5f51f28-f572-362b-b1c0-0f1a32941705 | -0.00246 | -49.95831 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9c155e4-b5ef-3c0a-aef9-e17876e5e6ed | -2.81132 | -52.95194 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0924b776-414e-396f-a233-0464a2f80491 | -3.81111 | -47.79345 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 366941a6-705a-3007-86d2-67371fb7651a | -4.3022 | -48.61852 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81a813d6-d10a-355a-8872-b34f4a3c8c6b | -3.9272 | -48.32833 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67d6d86-3998-3f5b-a2c9-2ccc407b5bc2 | -3.79971 | -44.02219 | 2024-11-08 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 907a7d38-b1dd-36f5-a488-49a678ca4f22 | -2.96383 | -53.8653 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91e98942-e312-3295-ad0e-d027d3766a72 | -1.49265 | -54.39025 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc23b2ea-8a21-3265-85fe-51a3460b358f | -1.62933 | -53.44242 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7729b09-8ec0-3a1e-8cd2-027a0463d1db | -3.71576 | -49.00257 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a1fb6d5-fcce-31a7-acf7-1e52a22f5f46 | -4.15647 | -48.24803 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f05c2afb-a77e-33e9-b78f-e2dc6cf8664a | -2.72835 | -51.71922 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2474836-e4c4-3426-a129-15ab0b6e515f | -3.96024 | -47.09127 | 2024-11-08 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 721a9699-e9e5-3bc9-bf44-df9f2af5af16 | -0.92799 | -47.12735 | 2024-11-08 04:53:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 87964a81-7806-3a96-9c49-f096cd9a480c | -4.61272 | -49.58017 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f5954a2-4a8b-32ad-9a4c-5b0f21300037 | -4.31567 | -48.62954 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b3f37ef-d6d4-31ea-aa6b-ce868bf968c1 | -2.18757 | -50.82108 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d73d28db-c8bd-33e8-9b67-3dac267ae404 | -3.06669 | -54.77937 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 827da355-9d15-3db0-9660-cb2a37841bff | -1.87355 | -54.18593 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebdd05f8-9542-39ad-87da-b0eb45178106 | -2.81411 | -52.95596 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9652f4b-c6a8-30a8-922f-d9c6997dac85 | -3.03889 | -51.53903 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 215020b3-0590-3349-8f3a-2ef69f303ce0 | -3.91408 | -47.95709 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c27be6c1-b42c-30f1-864b-add94d2a6815 | -2.46156 | -57.91356 | 2024-11-08 04:53:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a15a0ca-e5e3-3467-8c34-bee5317e3b92 | -2.58095 | -54.00078 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0581efaa-cfec-3ec6-afb6-9503551a8b64 | -3.00193 | -53.44666 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f87fe52e-2290-3ca5-9f67-11fdb072842e | -3.50398 | -48.23127 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82b4f358-6ac0-391a-b56a-7044d8a938ab | -3.96069 | -48.13322 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73aae926-aad4-3c61-9cf5-2b8b596647d2 | -4.02081 | -48.29972 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1077c65-ae68-3109-9db8-f7e42751aba6 | -2.674 | -53.02446 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7d93baa-f5b9-3a8f-8224-ee19c3d79779 | -3.23079 | -53.39811 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f950cb2-32f7-3f69-9a62-a989bfb0ff08 | -1.1615 | -54.07518 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d20bb999-fdab-3f7c-a8d3-f1f16a68723a | -1.34738 | -51.41212 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37a73ee2-1ae6-31bf-a4e2-c995d8e96c9b | -2.76637 | -54.04851 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cf6f6ef-dbcb-3460-aaae-b5076ed76847 | -3.29957 | -52.11465 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 158697d2-1994-3807-8842-1ebf86f549cf | -3.02359 | -53.86662 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f410c1da-04e4-3cd2-b5bf-1db5fe396c4f | -3.79472 | -44.02151 | 2024-11-08 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6dac169-5aae-328f-8905-4a31f1935dac | -4.733 | -43.24951 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ddf8278-a248-3437-83c0-83c45a677d0c | -1.54591 | -54.26045 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72e7be66-2213-3ce6-9c73-662cf3d37f8f | -4.82585 | -47.31836 | 2024-11-08 04:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d8de1b5-60a8-3578-9888-000b6d57cca7 | -4.94028 | -48.24059 | 2024-11-08 04:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 575b3bf4-fbb8-3f08-95a2-0c2c3cadfd23 | -4.22051 | -45.74548 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbab96ce-6df4-3670-a05b-7a7495549be5 | -2.21778 | -53.72072 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e63a8b1a-78e2-3f35-8910-22ff1a77f53b | -0.51721 | -58.09881 | 2024-11-08 04:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afbbaac9-0973-3d58-88bc-cf89bbdec876 | -1.34074 | -54.62148 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2bf7b02-4816-315b-934c-c471311500db | -1.20673 | -54.20516 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b075e7d-6862-3278-81b8-0a12505b8ea8 | -1.34791 | -51.4087 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19539bf1-148c-380c-81a8-33c8ef537086 | -5.635 | -46.9682 | 2024-11-08 04:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README28.md)

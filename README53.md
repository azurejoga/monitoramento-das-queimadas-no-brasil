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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4d89436-d099-38c6-adbf-2ce58bb005ed | -13.39174 | -46.8766 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcfbfbc3-eb85-328c-ac75-aacfe52072bd | -13.55987 | -46.86726 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbd07d28-12e6-352d-a32e-131441addf88 | -13.14145 | -54.92555 | 2025-08-29 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772e469d-ac11-399a-9ba6-4ea4ce278486 | -15.04608 | -48.13249 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 405486e7-612d-3534-92fd-203c140ca2b4 | -15.54267 | -54.27098 | 2025-08-29 04:42:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 756fbb4a-2146-39c4-95fa-3ebd62c30644 | -16.5124 | -45.10294 | 2025-08-29 04:42:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c25a3171-6da9-3214-9242-333c871f8934 | -14.26737 | -53.22976 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be9eab2c-94fb-32a9-bae7-7cae6bfc713d | -17.75698 | -44.50263 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fb52f75-2dc4-3332-b61f-94c61f4f0ffc | -19.73572 | -45.84594 | 2025-08-29 04:42:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf56b812-8444-3127-a896-1d8180d60a51 | -15.16893 | -52.33562 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f56403c-0c73-314f-b7a7-0c8a9de3726a | -14.59479 | -54.52209 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 093036b7-71c2-327a-936a-2ab20b35d513 | -15.30067 | -52.81101 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c04890d-0224-3a91-9b46-d48db3d7e8cb | -14.62631 | -41.73918 | 2025-08-29 04:42:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c071820-3414-3b3e-b23c-4c88a0d7099a | -15.67952 | -52.75939 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 575ee043-3a7b-3770-8a83-13ce49fd7861 | -13.63243 | -48.20256 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 97dd2b55-5461-3df0-816f-9e1a06391aa0 | -13.39951 | -46.9901 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| efdcba74-a1a4-32bc-ab9d-9689ac667050 | -13.82165 | -52.75314 | 2025-08-29 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ae1db10-b6d8-3539-9b72-821f03a9ac85 | -13.0219 | -56.91716 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d84d8e7-a4f3-383b-a701-7cd67be1f66b | -15.11522 | -48.57035 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52dd5da4-206e-3d7f-b71b-c7577fe4d039 | -13.68621 | -46.90614 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c95bcce-bf00-3e08-a00f-7325225402b8 | -13.98504 | -46.32978 | 2025-08-29 04:42:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89849217-8b91-3e1e-b54f-dbba0eafa45a | -13.639 | -48.20779 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17494ccd-9e44-3af3-84fa-e15c145bd44a | -14.29949 | -51.94054 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 874a35e4-04f4-3340-9452-92163b71e6a4 | -13.62238 | -48.24759 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7be8813f-64c5-306d-8fba-71807a7b3170 | -15.04667 | -48.1282 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bb6bb90-9cac-3672-b919-967081608dbb | -13.50083 | -46.83983 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc6cfd34-0db4-38d5-b424-61e448125399 | -15.12655 | -48.11723 | 2025-08-29 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d60d1fe9-7c49-338a-98f0-c104e8ad2c40 | -13.56894 | -46.85863 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19f8e61d-4e79-3e96-80d6-e869c7861184 | -15.17283 | -52.33255 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8327dc4-4dd5-3e03-92fd-3c4f476f1e7d | -11.72927 | -61.75835 | 2025-08-29 04:42:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a05bdf3-22b7-36f0-b52f-5ccc3296f85f | -13.45414 | -46.9616 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12818800-9ab4-3a17-800e-a250bcafa7df | -12.43875 | -63.92044 | 2025-08-29 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5c82cc5-a693-32e1-ab52-a96dd19c0a29 | -14.34741 | -53.23183 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2da11f7b-d981-3828-9306-28b14aa04f4b | -13.02606 | -56.91801 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab18c437-4dfd-357f-8b54-0b673bc62665 | -13.03023 | -56.91887 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b6589d6-3236-39bb-a5a9-52d3b3db4d75 | -17.5412 | -46.62108 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ddb863c-e878-35c2-bc6b-6ce92cc9c896 | -17.6037 | -46.68877 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fed1646-b5b8-35d1-b799-e785128daf10 | -13.57595 | -46.86463 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe45a3a2-0c6b-3614-b57c-a94133b64292 | -13.36759 | -51.76725 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a243bced-7c3c-36f2-a991-a2b88d971bb2 | -15.10455 | -47.87265 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dce32e2-4fae-32bf-8fef-c40afe001800 | -13.60152 | -46.86561 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8892a12-cfbf-36f0-a842-52675b262de3 | -15.1988 | -52.34063 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c920b0e-21e0-39f1-9c86-108e74562550 | -14.32825 | -51.93067 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42a25175-c92c-3177-acbb-140c0cc72e32 | -12.42561 | -63.91756 | 2025-08-29 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 87caaef9-423c-3371-b970-45848058ba21 | -13.48614 | -46.84634 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e56bdc4-e631-3c60-bd4f-ed0dc94a277d | -14.36137 | -52.10804 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c963216a-af7f-31ba-80a3-186231891767 | -14.32132 | -53.05032 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d5fb57f-afdb-3131-9e37-36f98d6b66b1 | -13.01284 | -56.91945 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7be32d51-969c-301c-9061-3e37b256b763 | -12.99467 | -56.92426 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8c63a93-ec05-38cb-8833-f06964c53836 | -13.6289 | -48.25311 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37024006-16bb-34c2-9dc5-bf0342793f84 | -14.24865 | -48.06634 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5501ca5d-aef5-3447-9c7b-413872690850 | -19.91268 | -43.84338 | 2025-08-29 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59396c9e-e4b5-3aee-940d-aef560ebfdd1 | -13.54173 | -46.8848 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5d6b2f1d-269b-39c9-98cc-8d17e76a2612 | -13.00795 | -56.92261 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42841c9d-a40b-31ba-8a41-8fab96e5e814 | -14.59123 | -54.52143 | 2025-08-29 04:42:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46c76910-0b98-3eee-bf31-ced966a81efb | -13.54959 | -46.94063 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 34244485-636e-36be-af9f-cec8804c1c58 | -13.59206 | -46.86186 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 120665de-a506-3a92-a0c1-96cf56bc1ea7 | -13.35372 | -54.38606 | 2025-08-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1f47d16-a379-3cd4-86e9-74241fded961 | -14.29825 | -53.29715 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e74b385a-dad0-345c-8d43-a7ea8c776577 | -14.33783 | -48.6513 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 562b8740-b9b9-3359-8d80-6acf1f9dd298 | -13.45854 | -46.84716 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f94de84b-1fb4-3d02-9070-cb83dfd78f6d | -14.23368 | -48.04119 | 2025-08-29 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1687a59f-ad9c-39c2-9776-946c35bf8bbd | -13.50402 | -46.84525 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2e372ece-ce49-33ea-94e1-9199c8f725ee | -15.66678 | -52.75345 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa12ec63-bce3-3a15-adb0-c899a5476272 | -13.68485 | -46.903 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cab5150-2683-34ab-a4a6-cceba26ced20 | -13.50725 | -46.85032 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1008e2b7-de62-32e1-aab3-6dd42f3b27bc | -13.41466 | -46.96525 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16b1749e-8f7b-3259-bf15-af9efd0317b9 | -17.60321 | -46.69254 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 872384ca-0c7f-3611-9698-dbc9d3231a67 | -12.51962 | -53.81559 | 2025-08-29 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3d9b9b7-9668-3dbf-bd66-da6d583d1419 | -13.52123 | -46.94796 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4b4ce9b-c753-306e-aabd-5aab973f50cc | -14.32409 | -53.05462 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06f03a60-7330-3d64-8850-db1a4e1ca714 | -13.54629 | -46.8802 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1972dd51-ad08-33ab-8b7f-8f9cabc3f55c | -14.30165 | -53.29773 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71147f0e-e892-3001-af02-ac540dcf45bc | -15.19274 | -52.33593 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f044280-a8af-3646-9151-3c196ae86d20 | -13.37202 | -51.7607 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1669e728-57e4-38c4-b769-1667d2532dbf | -13.64568 | -48.16068 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c039f2e0-2360-3709-9bb8-58d2c28f1044 | -15.7854 | -43.34897 | 2025-08-29 04:42:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6858842-d48a-394a-af64-f8001dbc30d7 | -13.41224 | -46.98253 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba803511-53dd-3553-a936-67db0d3c5de1 | -17.54218 | -46.61336 | 2025-08-29 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2573fc73-c0e7-3655-90fd-9174d88bf87d | -17.75252 | -44.50745 | 2025-08-29 04:42:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 59ff00bd-fd47-33d7-b3aa-e1ae45e12b03 | -13.58996 | -46.86403 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b61440ed-fa0b-38f7-9faf-892d8e80d406 | -12.99887 | -56.92499 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1c8e64c-4b33-3cb5-b1c5-1e46243e588c | -13.55275 | -46.94598 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 646b3ecd-accb-3535-9f11-b2c363eebda6 | -13.56439 | -46.86305 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b1316e5b-9013-3f26-86b1-9d218701d391 | -13.6396 | -48.20356 | 2025-08-29 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef7803e9-8359-3543-ad3d-11561f0ede58 | -13.48473 | -46.84277 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf9d60cf-1e8a-3ea2-b82e-603c67a0cd22 | -13.00098 | -56.91331 | 2025-08-29 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eadf1320-28a2-3c3e-9dcb-ea414ca1f4f0 | -14.3162 | -51.89947 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92f480f0-5287-3d13-adc3-750ea7eda705 | -13.55418 | -46.93581 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44b3d681-01c4-3fb0-b73a-b1fd276c380f | -13.66296 | -46.87595 | 2025-08-29 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54593211-a935-3490-9d59-b8622ed3cadb | -13.36871 | -51.76015 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a827e77-f7f4-3553-b120-48d25dffedbe | -15.67286 | -52.75825 | 2025-08-29 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53d5023a-b548-3b04-81db-a46d0394a662 | -13.60085 | -46.87054 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddde76ab-9905-3636-a065-81dececdc927 | -15.09955 | -48.39444 | 2025-08-29 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4ab4ca7-4795-3500-a2a5-c1a917a0cbbd | -13.40831 | -47.01068 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82ff37d7-9ee8-310e-b2dd-f4954457850e | -14.32381 | -51.93725 | 2025-08-29 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 936e1a41-28e4-3560-9373-8c2591642cea | -14.33355 | -53.29538 | 2025-08-29 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b15b812-d9f4-3b48-9820-a7125356b618 | -19.73628 | -45.84121 | 2025-08-29 04:42:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab2b6448-5616-3cfb-a2d8-2223eaecbb32 | -13.36702 | -51.77079 | 2025-08-29 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63972be3-78bf-3a9a-a4b5-16e80dc65363 | -13.56825 | -46.86357 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README54.md)

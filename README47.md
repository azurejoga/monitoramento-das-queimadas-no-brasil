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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bab61828-d404-345b-b156-141ab70e33ec | -12.93145 | -46.30639 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7fdfdf0d-64bd-378a-aeb1-fc1ef53459c5 | -13.5832 | -48.1974 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ba6ec65-6d1e-3c1c-aafd-623c819ff1af | -12.48673 | -47.23295 | 2025-08-26 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32bf72a3-c677-36c3-9140-a350de52a390 | -12.75945 | -48.13065 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5f50ed9-e755-36a3-9bb3-1626defde64e | -14.24543 | -48.03952 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b529167-0386-37ce-a61b-5dec2b7aaec4 | -12.41424 | -46.49072 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6afcdea1-07aa-3fa7-8306-a101c0cc0a5e | -12.73369 | -48.15761 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 501feff3-770f-3275-ba5a-e97f6155460f | -13.60857 | -48.19363 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbdf02ec-d098-3bd6-8878-3498469e2032 | -9.16141 | -59.46492 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1102337c-abd1-3c39-a035-67a26cfb007c | -13.05774 | -46.31582 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a322672a-bbba-3d62-8c95-a612d2cfa605 | -11.06101 | -52.00535 | 2025-08-26 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4844bc2b-32f9-39b0-a959-b6d2feb1c582 | -12.93534 | -46.30338 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e727c8b-8906-3d34-8712-c01d02ea86c5 | -12.73714 | -48.15825 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dadb394-6ef2-391b-a4b9-dfff7433d0c3 | -11.62672 | -46.21249 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f2252d1-eef7-3bea-b7f2-152d659de809 | -9.15926 | -59.51612 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02684645-df23-378d-ae7a-5ded7ad3b20f | -11.53373 | -52.1337 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4dfc8474-adfa-3a16-aee1-ae17a2a19248 | -12.92757 | -46.3094 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b41542c-4d13-3c0a-a210-32be8a99d82c | -9.17676 | -59.50417 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f797efd-035e-38f8-9ab6-382e077fb58f | -13.61608 | -48.14789 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63cf29ee-34fb-324b-9288-ce5699848590 | -15.08972 | -48.57235 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14df581e-9783-3911-8d30-e8e62979e01f | -12.70426 | -47.88644 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac72c06b-5cb2-3a11-ad0f-690c29afd1de | -9.1845 | -59.46209 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ebc18bac-dc2c-32c0-b5ed-d4c74d40e503 | -14.97479 | -52.88137 | 2025-08-26 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8acdaac9-cae9-3b73-93f8-3779b0d16f1f | -13.43661 | -46.86799 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9946c42b-d60e-3614-b7f7-bff18d454441 | -13.19377 | -47.20143 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33643086-4bc7-348f-81b4-a32ddfe6c7e7 | -9.16349 | -59.53233 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 01221aa1-51cb-341f-a76a-c7ff21e32946 | -11.57195 | -52.12307 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fbe544d8-1834-363b-9edc-06d7e2abfc6c | -15.63162 | -52.72052 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5576538c-b6ef-3c0b-855a-cf3e496f6201 | -9.16926 | -59.54107 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 462a5ca0-9182-3e06-9075-e1a248856708 | -15.08627 | -48.5718 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3559ef4-db3e-3e6c-8be1-3791767b8a7e | -11.64064 | -44.85556 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e776cf8-82b0-3672-b5a0-95ce1c1e05b5 | -12.39155 | -45.00724 | 2025-08-26 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0d5bc2cd-1c7c-351d-95d4-9e9bc00fbb2a | -13.42363 | -46.90604 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 314a7d0c-d3da-344f-a646-4e313dde4a3d | -12.74403 | -48.15966 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7be7efce-1a52-3668-8a60-9eefe51609d3 | -14.11396 | -53.98202 | 2025-08-26 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b32e1df-bb29-3b40-ac96-d7fe6f7dffc9 | -14.28964 | -60.35323 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab593fea-23d3-3450-a602-3aca6ef30dab | -16.6047 | -49.38121 | 2025-08-26 04:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4b4f81b-3414-39a0-a794-0fd15c6c8f0b | -12.74684 | -48.16419 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bc0f3488-70c6-3168-974b-5fce34c726fb | -14.7739 | -47.92806 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bbfa4e8-0eec-348f-a757-a54c5b580f02 | -13.4487 | -47.00605 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd29c3e5-226c-3a17-98a8-475125a76a50 | -9.17151 | -59.45181 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e7e68104-b9f8-3d3a-9ed5-1f6006a55127 | -13.45055 | -46.86655 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92e1b729-9605-3780-a0ae-1f05a38ab097 | -13.52553 | -46.90475 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 34a8a443-8e20-37aa-92dc-e8ce8a273ae8 | -13.66109 | -46.88292 | 2025-08-26 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6e00b28-9910-33a2-978b-b33c14f45cd3 | -13.46103 | -46.99341 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e04fa4e-a574-36f2-b252-019b69abd615 | -13.41762 | -46.87949 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bded3129-4e47-3f07-b67e-4c5c3843cd30 | -11.29965 | -53.96244 | 2025-08-26 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ffbef68-3ff2-38ae-8335-2b704f9e422b | -13.5261 | -46.90116 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78426bd0-3be6-3c46-a353-316afb83620a | -15.12517 | -48.67841 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6edeb62-e392-3ea9-8f8e-bb2ecf19ab8d | -11.63283 | -44.86164 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae7b905f-dd37-336e-90f7-61b51bfa9f68 | -11.63287 | -46.40981 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6402a7da-8d49-3a0c-8c55-11f40421b4e2 | -14.44487 | -56.46327 | 2025-08-26 04:23:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a377c0b7-bf07-3b45-a8eb-06f775e226a4 | -10.39486 | -57.69927 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 437b02c1-02c3-3060-b0ed-70047c4f457f | -14.26096 | -48.0302 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c66e0b15-bf62-3d15-a6f9-324be530ee02 | -14.3326 | -48.64774 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23b64233-76b4-3e50-87f1-790e47c3d7a6 | -11.55085 | -52.11451 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 180d5b89-b812-3d58-92ac-b3fd940c6615 | -15.11463 | -48.72029 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a9418bd-15b0-3ee7-967c-ca78fa0f57a0 | -13.48601 | -47.00904 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96344efa-e372-3987-8e70-54cf733811ce | -12.3882 | -45.00671 | 2025-08-26 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3df4171c-6429-3fdc-b988-521ecdb9c3e3 | -12.67709 | -47.86314 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9391375a-fee1-3793-b5be-1b09eca9cfe7 | -9.16998 | -59.53588 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 55ee7884-8206-3ba0-bffe-ab13d2c8d28c | -11.56273 | -52.09898 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98249bb7-3ff7-34e7-8c12-bf291b6fdfbc | -13.59352 | -48.19912 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c51dbfb-4a76-3f5b-a16e-180798a32159 | -15.08263 | -48.55136 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c63775a-becf-3ddc-a33f-8e2e9ad8a389 | -13.4335 | -46.92994 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f54453de-05ce-3578-a131-b65292e1eb67 | -14.25814 | -48.02605 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9edd208-2d25-3435-8cd1-e331d7761a2b | -13.62873 | -48.14916 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff11a47e-781b-3ea9-919f-730105caaa3d | -12.76289 | -48.13134 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 936f8f25-254c-37e8-87b0-cf61dc5d5135 | -15.11809 | -48.72091 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aceedcc6-e7f4-3976-934f-be94558a161a | -12.98995 | -45.22298 | 2025-08-26 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3bfc47d-0610-3bd8-9813-879d00783f78 | -12.93202 | -46.30283 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 784591e1-4b1a-3c00-8a15-1f7a69b360bc | -13.05994 | -46.32346 | 2025-08-26 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8a61a1e-f99f-3052-a8f5-879125fbb733 | -15.40912 | -46.5902 | 2025-08-26 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25e4d825-3d17-33dd-b08b-4b0a2baa3500 | -15.08197 | -48.55529 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bfdd0b2-25f2-3b36-8c2b-374c6ced1dc4 | -13.45262 | -47.00298 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49498941-bcc6-3bcb-8ef8-b616a1085d2d | -13.41738 | -46.92353 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18290fe7-f3db-354b-a870-e8dc7dd6d793 | -12.70272 | -47.87453 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d195ac14-6ea3-34ec-aa12-022c900373e3 | -12.93365 | -46.31406 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f157d539-e23a-3fe8-b494-b1de69e6c41c | -16.60121 | -49.3806 | 2025-08-26 04:23:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2190b1c-c447-3d3c-ac62-8c80ce02e3da | -13.41694 | -46.90503 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 345a9d1d-63d6-32cb-979f-b2578180ed7c | -11.55208 | -52.13259 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02151f40-7e81-333b-9635-b9218ecb2d22 | -13.51768 | -46.91085 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b24d653-4bcc-3839-b463-070e10d77b70 | -15.08692 | -48.56796 | 2025-08-26 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64d9fa30-d08c-3b93-af8f-c247de4e8460 | -15.57281 | -43.85463 | 2025-08-26 04:23:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c2ca4b8f-d786-3d16-ab27-41755879ad0d | -12.77824 | -48.11275 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48ac3eff-d062-32c6-ad60-03c180f1eb0e | -15.02965 | -48.66643 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22ec818b-6a6b-38aa-b769-ca5468720063 | -13.40923 | -46.88902 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 250b5576-3e52-3c22-8c32-fd9c428fe2fd | -9.19393 | -59.53103 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 166d73b0-f906-327d-ae1a-5a1ce7f901a8 | -9.1927 | -59.49988 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b21e381-0366-3114-97fd-16de35e6cb4f | -15.1187 | -48.65332 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 462fd851-750a-3ad6-9807-54f8dbbfa219 | -15.10448 | -48.7384 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af09c3b7-1e10-32af-a6f6-92721b1ea60c | -9.17129 | -59.45715 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f73e9a1-a7b9-3139-869a-86c3982b62b2 | -13.41314 | -46.88602 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ba74dbca-c76e-3e72-a185-79bbd6e606ec | -11.04991 | -52.01662 | 2025-08-26 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a77e0641-3cc7-3fe8-b255-126700fbe2fb | -9.17288 | -59.52112 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2dfd820-6513-3256-8412-8e32e27aa766 | -12.78526 | -48.13443 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 763b1daa-a6eb-3a21-9363-71de7467f62f | -9.19692 | -59.51623 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45c2bcc1-2797-358a-a473-0047a8167f96 | -9.15103 | -59.55543 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0fdcf0da-c68e-3502-acf7-dd23c2557684 | -14.75784 | -59.72318 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a88a207-6f0c-3fc6-8b7f-106a8f3fe246 | -14.304 | -60.36747 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README48.md)

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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7463df63-9f06-356d-ba03-76e4d6f9ad83 | -12.0298 | -51.0722 | 2025-09-09 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f29c968e-8df0-36cb-bf34-4ef38d1af800 | -17.2762 | -46.7305 | 2025-09-09 12:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3e7c442a-7a36-3485-97ce-d427bb9eac2f | -19.8426 | -48.1718 | 2025-09-09 12:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 114.4 |
| cc8cfd51-f4f6-332c-bf1b-3a3af1d81d85 | -12.2941 | -49.9904 | 2025-09-09 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f48322f4-b560-30cb-8852-adb0f2eb2763 | -6.2224 | -43.3693 | 2025-09-09 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 10bec1d8-0f0e-3dee-b7c6-b490f260dfe7 | -5.5702 | -42.9062 | 2025-09-09 12:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| 45a2d083-56dd-319a-95d7-41afcaa1c606 | -11.3389 | -46.5419 | 2025-09-09 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 2fbe4f2b-9cfa-3eb8-ad39-fd3d0459b7f8 | -11.9926 | -51.0126 | 2025-09-09 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 308.9 |
| 7d0e862b-185b-3b87-bcee-a9766c5b2c9b | -12.529 | -45.2756 | 2025-09-09 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 64106dd4-6ba0-3b2c-807e-11bc8cb2dc9e | -8.4119 | -49.0869 | 2025-09-09 12:40:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5d7973c2-957e-3965-a263-eb0e9c35441e | -7.789 | -46.0891 | 2025-09-09 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d84ae570-2d58-3086-a0b1-d9c71527153d | -12.1988 | -53.9024 | 2025-09-09 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a9e2cd67-c894-36cd-a6d4-cf29dd652edc | -15.2492 | -53.7826 | 2025-09-09 12:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9dfc3f21-2d60-3f33-8872-4613f47f3e72 | -12.1991 | -53.8817 | 2025-09-09 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 622bb92f-35a9-3ded-8db9-2892ab9caf78 | -5.9191 | -45.7717 | 2025-09-09 12:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8c17bab3-3a92-34da-818f-fcbb1eb436e3 | -21.4555 | -48.8455 | 2025-09-09 12:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 74ef62f6-ba8e-3635-bc41-c6eee1d99847 | -11.9739 | -50.9935 | 2025-09-09 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 25e99c3e-a113-3e9b-83df-662f4454192e | -12.0291 | -51.1149 | 2025-09-09 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| caee7136-0801-3064-b2c6-d66a06e7fdcf | -5.453 | -43.4525 | 2025-09-09 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d938a148-3f97-3194-a2ab-702594adee3a | -13.8019 | -46.2663 | 2025-09-09 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a9351669-7981-3ec2-a99b-f41fef034f69 | -7.6746 | -47.9578 | 2025-09-09 12:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b1616be1-90e0-346d-919e-bdb8f14a168f | -17.2563 | -46.7346 | 2025-09-09 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 3f71d8e1-43b6-333c-9845-21e88b9f30a8 | -5.8406 | -44.0951 | 2025-09-09 12:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f08a7a31-c564-3070-85a0-03a0751f3946 | -13.937 | -48.2522 | 2025-09-09 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8338732c-a69c-3dad-a86d-6070550269d6 | -5.5702 | -42.9062 | 2025-09-09 12:50:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 172.7 |
| f4a77d24-60f6-39c8-9eb6-204fd22df052 | -9.7203 | -46.8526 | 2025-09-09 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 05c38098-6775-3d2f-b3b4-33793041a4d3 | -11.4277 | -43.6017 | 2025-09-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9c9abcf8-e25d-341e-bc0f-5cf293ae5a47 | -17.2757 | -46.7538 | 2025-09-09 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b311fde6-e105-3a8c-b854-0695404d9b15 | -6.2595 | -43.4129 | 2025-09-09 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 521947af-b5cc-3c09-8e46-2d519213c811 | -11.9926 | -51.0126 | 2025-09-09 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.5 |
| a18ecc66-65a3-3c91-8643-55a3a896633c | -17.2967 | -46.7032 | 2025-09-09 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 146.8 |
| c872b96b-f566-3c54-8043-dd8ed0636b3d | -11.3389 | -46.5419 | 2025-09-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 4c938b87-a00d-3a6d-9b99-4242a0f32f1b | -6.2407 | -43.4144 | 2025-09-09 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 106d44a9-63ba-351e-a6d8-6e81426396cb | -8.4119 | -49.0869 | 2025-09-09 12:50:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6571272a-7e2f-395b-b0fd-6ed85f9374a8 | -5.8395 | -44.2103 | 2025-09-09 12:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| b1498f9c-9a26-39e4-9e72-c160696e2ca9 | -11.446 | -43.6461 | 2025-09-09 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 7113977d-9085-3b9c-b2eb-9be30ad0409d | -12.1991 | -53.8817 | 2025-09-09 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| c1cfc894-530d-3054-9132-6191f7f6d5a1 | -19.8426 | -48.1718 | 2025-09-09 12:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| c92718fd-2ee8-3763-8da5-cc15fda2c9c3 | -17.2973 | -46.6799 | 2025-09-09 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 126.7 |
| c91490b5-4e71-3aea-b894-3f64dea027ee | -17.2762 | -46.7305 | 2025-09-09 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 962a64b4-1132-33e8-bdaf-2f85af30f27a | -14.5465 | -48.758 | 2025-09-09 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 22d109eb-ad91-3587-8ebf-0c0c32c2bb54 | -12.1988 | -53.9024 | 2025-09-09 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 00952229-d18f-3489-92d1-463b9f3d7c32 | -11.9923 | -51.034 | 2025-09-09 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4bfd3466-3b16-3033-bb8e-5107f2cd9479 | -21.4348 | -48.8503 | 2025-09-09 12:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 529.1 |
| 0684fbc4-5f28-3b61-9b9c-dc6dd900af71 | -10.2982 | -48.8148 | 2025-09-09 12:50:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| d93a433a-7982-356b-bcfd-3282d8129418 | -5.5504 | -45.1891 | 2025-09-09 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 22398486-5671-3ba3-bb20-8191c5a4855e | -7.8622 | -46.2616 | 2025-09-09 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b888f8a0-b7ef-320e-810d-56e978ce2833 | -19.8223 | -48.1763 | 2025-09-09 12:50:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 140.6 |
| dce24af7-76da-3624-a922-e46fbe16135f | -6.2224 | -43.3693 | 2025-09-09 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3bde1d3f-ddce-3bd2-a570-bda23965a925 | -12.2941 | -49.9904 | 2025-09-09 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2d1eca32-edab-38d2-8062-b5e173c82184 | -15.2492 | -53.7826 | 2025-09-09 12:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b8379fa3-dc1e-30d4-85b5-2f7c912988e2 | -20.0883 | -47.3502 | 2025-09-09 12:50:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 16ade359-9fe0-31ee-9c74-a8143ca88f0d | -13.9564 | -48.2493 | 2025-09-09 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6325e38d-3f08-3322-adf5-952418536d31 | -15.2683 | -53.8012 | 2025-09-09 12:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 988657fa-e034-34fd-9e7f-a90ea2efe2b2 | -21.4341 | -48.8735 | 2025-09-09 12:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1077.3 |
| 45084e0c-94c2-399d-a956-805e715c642e | -6.6364 | -45.107 | 2025-09-09 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 27deba9d-433c-34e3-9033-1357c64d07b0 | -11.0231 | -46.0412 | 2025-09-09 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 9d9f8180-7b12-3e68-86bf-9c48ab6d5561 | -6.199 | -45.8186 | 2025-09-09 12:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 117f3161-00d7-3d4c-9ca3-81ce20cb8740 | -17.2557 | -46.7578 | 2025-09-09 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| c96526a5-f582-37b7-a233-f0514c2cec96 | -12.0295 | -51.0935 | 2025-09-09 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 0619da19-eb0f-343c-8bba-cece4a2a11d4 | -7.6744 | -47.9796 | 2025-09-09 12:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 4aaf8763-c139-30da-a6d4-4425a39f38a4 | -9.0934 | -45.7088 | 2025-09-09 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 43533941-41be-35f9-83b3-a48dad710005 | -9.0931 | -45.7314 | 2025-09-09 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 370571ea-d097-362a-bb0e-71f7b25aea25 | -7.789 | -46.0891 | 2025-09-09 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 1e98da1d-9210-3483-a376-3c0ec1360720 | -5.589 | -42.9048 | 2025-09-09 12:50:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 174.6 |
| 3b9f0540-4800-3d22-a506-e2c8c8bd5065 | -12.2938 | -50.0121 | 2025-09-09 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 0797a728-a018-3548-970a-ca0849bdcf2f | -7.5611 | -44.6597 | 2025-09-09 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 38744045-6f9a-3a77-8a26-27eb6d5d3241 | -17.2762 | -46.7305 | 2025-09-09 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8a126a0d-00b5-33f0-ae6f-c9a9c4ea6e5f | -6.2407 | -43.4144 | 2025-09-09 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 132.0 |
| de5aefb7-98b8-3132-8510-e7b339b014b8 | -11.9739 | -50.9935 | 2025-09-09 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 660c33f0-5194-3c47-bd1a-2d9682ed5d03 | -11.4325 | -50.329 | 2025-09-09 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 574b510a-0f26-3a7a-92a1-0c8e2be2ef28 | -5.5504 | -45.1891 | 2025-09-09 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| c4132e1d-f980-39a1-9c5f-8dd94c2aed18 | -15.8205 | -52.2444 | 2025-09-09 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 080993d8-79dd-3170-8f51-24b41591d5d3 | -5.8406 | -44.0951 | 2025-09-09 13:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 983006a5-4910-3ccc-bfc0-66404f17259d | -11.3385 | -46.5645 | 2025-09-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 08f8c152-a7f2-347d-b0cc-77c49be4f3a7 | -12.2181 | -53.8798 | 2025-09-09 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d25fbf7e-7f48-3d72-8ac9-2ebfa93308c3 | -11.9926 | -51.0126 | 2025-09-09 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 5c4dbd1a-6162-3cb4-ae93-b2b53cd62f20 | -6.1899 | -41.0154 | 2025-09-09 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| d9ebe637-3a4f-3232-8642-e2bc9bfc3243 | -6.7851 | -43.4371 | 2025-09-09 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 898b867e-8ced-3fcd-b0ce-cb31a1d546ca | -12.529 | -45.2756 | 2025-09-09 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 18d3dbf5-5041-33ad-869d-b6f9156c8fe4 | -17.2967 | -46.7032 | 2025-09-09 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 5098f2ab-ab9f-31c8-ae61-b6f9562d951a | -12.0291 | -51.1149 | 2025-09-09 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| eb9fd05b-879c-3f88-8f4a-07c131c46024 | -5.589 | -42.9048 | 2025-09-09 13:00:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 214.6 |
| 225623fd-ac48-356f-8996-8549408c5f43 | -6.2087 | -41.0137 | 2025-09-09 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| cd680790-8de9-3921-97fa-27fa1703f14a | -12.2938 | -50.0121 | 2025-09-09 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 17a0cb6b-9f43-39ec-97f2-edd7949e8636 | -11.4469 | -43.5988 | 2025-09-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| da0a19ee-d824-3586-a7b7-d357d744012a | -8.4119 | -49.0869 | 2025-09-09 13:00:00 | GOES-19 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1ffed616-53c1-3be9-b9bd-12f42a91a204 | -6.2226 | -43.3459 | 2025-09-09 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d65dd5f6-2a5b-345b-839e-3e97f166230f | -12.0295 | -51.0935 | 2025-09-09 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 907dfe74-f307-3e01-bee8-03fe1e102b42 | -12.18 | -53.8836 | 2025-09-09 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3b19c66c-a9f0-387f-be25-00278e595b9b | -21.127 | -48.8519 | 2025-09-09 13:00:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 158.8 |
| 273b1c53-a817-36bd-8616-9c9fc31288be | -5.8395 | -44.2103 | 2025-09-09 13:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 88c97771-96f0-32eb-a992-0fec3c814a81 | -5.9901 | -46.1917 | 2025-09-09 13:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 44d2185e-bf14-382a-bd64-442ab0510d0a | -11.3198 | -46.5444 | 2025-09-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d9e9903d-084b-3c96-9fba-b32b985fe88a | -12.5295 | -45.2524 | 2025-09-09 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 343d2574-892d-3914-b8bb-5147a4dfddc8 | -11.3389 | -46.5419 | 2025-09-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| e2b53446-b85e-3434-9867-5c9e12485cc5 | -11.3549 | -50.4447 | 2025-09-09 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 22d86b80-46d8-31e8-8578-1b4a151ee4fc | -5.8582 | -44.2088 | 2025-09-09 13:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d4bf8dfc-5941-3705-bf4e-62caf619cdcb | -5.8791 | -43.9769 | 2025-09-09 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f4dda28d-1dcd-38d8-aacc-407d585e91a5 | -12.2941 | -49.9904 | 2025-09-09 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |


[Clique aqui para ver as próximas entradas](README77.md)

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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48d28e36-4fea-3e16-8c6b-2d4073b3fdbe | -12.379 | -49.9888 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4cddb60-c2ab-35ee-9f92-8600f22de80f | -20.451 | -46.384499 | 2025-05-24 00:37:00 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a898a853-a651-38cb-944e-2ecec761cae0 | -23.170401 | -50.1758 | 2025-05-24 00:37:00 | METOP-C | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 990a4d53-aa82-3d1f-862a-2987c09bf976 | -6.234 | -43.3549 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5e6eafe-6726-3b7a-b216-a4bae3df9da9 | -21.3216 | -49.479698 | 2025-05-24 00:37:00 | METOP-C | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35e1dc0e-38e6-3b26-a83c-b1d3a08e5a07 | -6.2219 | -43.347698 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcdc58da-222e-3179-bd9e-ee193781a414 | -4.296 | -48.2742 | 2025-05-24 00:37:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4bb5da3-643c-3719-9f1c-cefddc777ca4 | -8.0859 | -43.1152 | 2025-05-24 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3681e5d3-3c75-3e80-a862-011b79c0a07f | -11.1463 | -40.336899 | 2025-05-24 00:37:00 | METOP-C | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0967596b-405e-3776-9fbd-615ea984c7e9 | -9.078 | -49.665501 | 2025-05-24 00:37:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc2ccff5-dfc5-30b7-aaaa-cbdb0207893b | -12.4005 | -49.9935 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c00d395e-1373-34da-a447-cd0d0a8d4743 | -7.5385 | -45.8288 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c60f0ee7-aac6-32ac-b2fc-6620ec40b9cc | -7.0868 | -46.061199 | 2025-05-24 00:37:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5883a8c8-e456-3f91-9ee9-369bc328c5ff | -12.8435 | -47.3992 | 2025-05-24 00:37:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1d8ca23-f7da-3474-9b2b-e9513e7f38c2 | -11.1623 | -40.359501 | 2025-05-24 00:37:00 | METOP-C | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e783ce36-1546-38a6-99e3-af6d01af090a | -9.1222 | -47.653 | 2025-05-24 00:37:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 882474f5-7f7d-394c-9723-3e2618904241 | -10.4916 | -42.424198 | 2025-05-24 00:37:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 59d02881-ced9-33a2-9216-809ae2a27d99 | -13.3736 | -54.271599 | 2025-05-24 00:37:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 852bcb44-ce56-3427-bd66-5e57318688bd | -20.4478 | -46.368801 | 2025-05-24 00:37:00 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 108b790f-37bf-3615-99ba-6ab8d9ff2836 | -6.2264 | -43.366798 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 701c3f2e-3ca7-3392-8862-80f73603af67 | -7.0722 | -44.936699 | 2025-05-24 00:37:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0da908a8-ac24-3ea8-8d56-2aca7f90b44e | -13.132 | -56.8064 | 2025-05-24 00:37:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6f201b1-e95e-3972-8cea-12f5037ed032 | -12.3541 | -49.9198 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a374bccc-3b43-32e3-928c-015d394a6335 | -20.9347 | -56.554901 | 2025-05-24 00:37:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4de31ce6-39b9-374b-97bf-aac6c49e3868 | -12.3967 | -49.975601 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d648f5e7-86e1-36f7-b755-11bfa671c52f | -21.0599 | -42.953098 | 2025-05-24 00:37:00 | METOP-C | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 932f5533-48d7-3c7c-af68-aedb5ed1b729 | -7.5402 | -45.835999 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbc8f1d5-3fe2-3ae4-a2db-36716bb53ffc | -11.156 | -40.334499 | 2025-05-24 00:37:00 | METOP-C | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 954656aa-c78f-3295-9baf-052f676770fc | -8.7556 | -48.036201 | 2025-05-24 00:37:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c045016c-e263-32dc-b788-b82a660092cd | -10.3484 | -46.653301 | 2025-05-24 00:37:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c76a242d-6943-3a3b-9d31-f1978b7de96c | -10.9513 | -48.1436 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0c6226-6772-35bd-896c-a49741d8b78d | -13.3605 | -54.256199 | 2025-05-24 00:37:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f178493-e55b-3e75-b045-771dca83b4d2 | -7.7959 | -46.2272 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4604a6f0-9792-3feb-868b-c9b6dc2e190d | -10.0365 | -48.701801 | 2025-05-24 00:37:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54ae01d4-d36f-38a5-9dd6-7cc634f3a3f9 | -8.0739 | -43.108299 | 2025-05-24 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7f4cfe07-5ef4-37c4-bb32-46227def385c | -7.0851 | -46.054001 | 2025-05-24 00:37:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca7f968-72e9-33d7-9705-8d14a3697001 | -8.0881 | -43.124599 | 2025-05-24 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 24b78784-f37b-329c-8dfb-1a76cab83c20 | -20.4494 | -46.376598 | 2025-05-24 00:37:00 | METOP-C | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9f20b263-c67b-30ef-b6d4-dfd200222fca | -10.9545 | -48.1581 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4543ed39-c1d9-3ab1-b3b6-d7de9aa2362e | -12.3809 | -49.9977 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6cf5605-1889-3ca8-b106-854b468c0236 | -10.7258 | -52.472099 | 2025-05-24 00:37:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd5a984a-cf44-3c68-8f6d-38cfa4360c5c | -12.8419 | -47.391998 | 2025-05-24 00:37:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c61b508a-591c-3364-8917-ecb6c0523dbb | -20.939501 | -56.586899 | 2025-05-24 00:37:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0adef6-e919-328a-a64e-ae8d5905b1e1 | -13.3703 | -54.254299 | 2025-05-24 00:37:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b404de94-f910-3f90-96c8-c640f60dd184 | -9.0797 | -49.673401 | 2025-05-24 00:37:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8abdb3d1-1150-39f9-bc80-641ac6125a00 | -13.1417 | -56.8046 | 2025-05-24 00:37:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3f268af-e505-35a9-88e8-109ca242971d | -13.1513 | -56.8027 | 2025-05-24 00:37:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 975f6b3d-7fac-3363-987e-dcf6764b2bc8 | -10.3611 | -47.9883 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6233b71-79a7-3053-b857-9cbd2132d374 | -12.0806 | -47.346401 | 2025-05-24 00:37:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c54304fa-dcb9-347f-ae8a-db373e16153d | -10.0348 | -48.694302 | 2025-05-24 00:37:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c77e7b9-d923-39c6-ba61-54437f47490d | -8.0761 | -43.117599 | 2025-05-24 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 292b470d-b46a-32b2-b618-b3643ed9355a | -7.5483 | -45.8265 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb9a46f1-d63e-372b-a88b-e711d7efdd0a | -14.2397 | -44.6376 | 2025-05-24 00:37:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be542202-cc4f-3c23-9cf2-52cce0b339d6 | -6.2362 | -43.364498 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fee794c8-eaa6-3477-850d-5b06d0a638ce | -11.7467 | -54.230701 | 2025-05-24 00:37:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d25fddb-c021-3979-8844-2f68d9fd3a84 | -10.9529 | -48.150799 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec2ca64-5c73-3398-8aba-cacd6d91320f | -11.7532 | -54.212601 | 2025-05-24 00:37:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6679ff14-ff6a-35c6-aaeb-a5e53ae5b7ce | -10.3693 | -47.978901 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e189fbd2-13b0-3565-b69f-67c2eb7e5de1 | -10.5013 | -42.421799 | 2025-05-24 00:37:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9637c9db-19f8-3221-b65f-5f22673b50e2 | -12.4065 | -49.973499 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69deae21-bf29-30a9-b76b-0e795a7edfde | -7.0835 | -46.046902 | 2025-05-24 00:37:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba113de0-86d2-3920-a78c-6d7d8402fb72 | -10.4641 | -47.942699 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a486310-b837-36ac-9ed6-1acee03069e1 | -12.3579 | -49.9375 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f00cd593-0fd5-31e5-8968-7c8ef3b1477e | -10.3709 | -47.986099 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5c8c45-4024-3543-958a-15c646fd1c22 | -7.6636 | -46.101299 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e713a74b-3783-3777-b924-863c6690fb8d | -11.1592 | -40.347 | 2025-05-24 00:37:00 | METOP-C | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2fe860ac-2e43-300b-92b2-c09ed67a3502 | -12.3986 | -49.9846 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 300f6c8d-d9cb-32c7-bcab-005256e0e82c | -20.929899 | -56.588501 | 2025-05-24 00:37:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cf41456b-2243-3e0f-ad5c-3db1dabbce53 | -11.8031 | -44.2845 | 2025-05-24 00:37:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da326834-0dd8-31e8-933f-5fae6e5eb73e | -10.097 | -47.0895 | 2025-05-24 00:37:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4f2b42e-f46b-388a-bb2f-a51b3feb97d7 | -14.238 | -44.630299 | 2025-05-24 00:37:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4eb0ca2f-660c-3924-b6bd-13e663562e2d | -10.4657 | -47.949799 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 028d484e-f7f0-36ff-b012-8a8bfe3cc57c | -7.55 | -45.833698 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e20a197-c931-323c-82da-9b892f16f9e1 | -10.3468 | -46.646301 | 2025-05-24 00:37:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf0a9e21-c152-3b3f-bd7f-4ed23a1fe446 | -20.254101 | -40.254799 | 2025-05-24 00:37:00 | METOP-C | VITÓRIA | ESPÍRITO SANTO | Brasil | 3205309 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0810b98b-ed63-3685-ad5f-47292b52636c | -14.2299 | -44.6399 | 2025-05-24 00:37:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d2f84a6-0d8e-3d7d-89f0-19c0ef10a1a4 | -20.9601 | -56.5967 | 2025-05-24 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f87e3c0c-b5af-37d2-a091-3ebfcf9cd804 | -20.9402 | -56.5786 | 2025-05-24 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6ffe6990-6b91-362e-b44c-fae55d2e165d | -20.9398 | -56.5998 | 2025-05-24 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4d9761c7-63d9-362a-a5e9-8daa3b9723d6 | -13.1498 | -56.8054 | 2025-05-24 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| eaec5285-8c84-3935-a3ce-86d6c95f8b62 | -8.0889 | -43.1196 | 2025-05-24 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| bb57208c-1dbb-3ccc-b38a-d8f6893afc19 | -6.2226 | -43.3459 | 2025-05-24 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 268075b0-38d5-366a-8d99-b7377c528bde | -8.0703 | -43.0981 | 2025-05-24 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| 3f7973f2-bfad-3570-8e70-c0919c679523 | -11.1425 | -40.3498 | 2025-05-24 00:40:00 | GOES-19 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 35406e8d-fccd-359f-9733-23e726d381b4 | -13.1496 | -56.8255 | 2025-05-24 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fa54a8eb-f8b7-3d3d-8f66-97e6effcde28 | -20.9606 | -56.5755 | 2025-05-24 00:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 04749cef-4935-3bc7-bbfc-c7c2c5d3edba | -6.2224 | -43.3693 | 2025-05-24 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1b8a08a8-7ed9-3f2b-b75d-d6d1a2ad58d3 | -8.07 | -43.1216 | 2025-05-24 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 32a03959-2a2f-3481-9288-a7d1f7cb88a1 | -6.2226 | -43.3459 | 2025-05-24 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 68e40f07-d513-3a50-b67b-75a04a9e1f82 | -13.1496 | -56.8255 | 2025-05-24 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1036b146-1017-33cd-94c4-26552528610b | -8.0889 | -43.1196 | 2025-05-24 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 4ecefce0-0e6e-3970-860d-62d893135961 | -20.9398 | -56.5998 | 2025-05-24 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5744f722-1603-3790-be4f-c1fca32b96f5 | -13.1498 | -56.8054 | 2025-05-24 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 8d605d80-2852-330d-82fe-f8b04218d4ec | -11.1425 | -40.3498 | 2025-05-24 00:50:00 | GOES-19 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 6a29c8a0-7c4b-3e09-bf95-0992e9011f42 | -20.9601 | -56.5967 | 2025-05-24 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 4d4fdc05-1c87-3d2c-b8e1-5f98431609b3 | -8.07 | -43.1216 | 2025-05-24 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 4c037dc8-5e73-3176-9c51-fa4210927b33 | -20.9402 | -56.5786 | 2025-05-24 00:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 48aabe9f-ad4c-38cc-9e98-0a220cfbf701 | -21.05473 | -42.96117 | 2025-05-24 00:52:00 | TERRA_M-M | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.5 |
| a01b6647-4eec-3407-831d-db9fe34f624a | -23.1772 | -52.11081 | 2025-05-24 00:52:00 | TERRA_M-M | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 98868026-0450-3f2a-8888-6b272796d038 | -23.1793 | -50.17579 | 2025-05-24 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |


[Clique aqui para ver as próximas entradas](README3.md)

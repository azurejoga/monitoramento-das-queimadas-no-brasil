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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 327c77e4-e8fd-346a-8371-7148194d2394 | -4.46756 | -48.12329 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aac4e1e-115e-3af9-bb1c-0a695e6a624d | -4.7559 | -47.99994 | 2024-10-17 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e32fe10d-f94f-39b2-8382-2673014ea519 | -5.66737 | -48.68091 | 2024-10-17 03:49:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 435d920e-47fe-3c52-9fd8-4af182daa1e8 | -5.66641 | -48.68637 | 2024-10-17 03:49:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 963bf81b-89a4-3199-8821-7122d7aadb41 | -5.22642 | -47.95634 | 2024-10-17 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f9752fd-9f49-3e34-9d7e-e1b307b99162 | -5.22877 | -47.95727 | 2024-10-17 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f18fe71a-9b42-37eb-837e-03bc6ceb6152 | -5.22789 | -47.96233 | 2024-10-17 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5ca6c5c-bca2-374f-bb71-d9cf0f653a3f | -5.22551 | -47.96135 | 2024-10-17 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 363eb3e1-62bd-340d-9b21-6919c28ad4b0 | -5.22256 | -47.95592 | 2024-10-17 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 567f668a-ed1e-32e0-9814-a1f9d7e1b647 | -5.22169 | -47.96088 | 2024-10-17 03:49:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d1e1eb8-4e9d-35a8-9038-6f4f7e559686 | -15.32444 | -52.98047 | 2024-10-17 03:49:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f312508e-69c8-3ad7-931c-453954bff678 | -15.31742 | -52.97874 | 2024-10-17 03:49:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2503e98e-9057-3ec6-a064-2cafd01162a0 | -22.30588 | -41.88295 | 2024-10-17 03:51:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 348d66c2-e6e5-3901-b059-d827b5344cae | -21.91358 | -42.26313 | 2024-10-17 03:51:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a5b8346b-d8d9-303e-9c10-2d08133cf8fe | -21.90445 | -42.02478 | 2024-10-17 03:51:00 | NPP-375D | SANTA MARIA MADALENA | RIO DE JANEIRO | Brasil | 3304607 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d81eb8d-827a-37dd-8a73-bdec7344734e | -20.9353 | -42.59264 | 2024-10-17 03:51:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a78043cb-44a7-3135-b87a-51dfbca282f0 | -20.93455 | -42.59693 | 2024-10-17 03:51:00 | NPP-375D | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7695c7f7-7ec7-3828-9459-5e9af9d79a29 | -21.6276 | -43.46832 | 2024-10-17 03:51:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74dec896-cd7f-3183-b700-7295d052f0a3 | -21.62717 | -43.46565 | 2024-10-17 03:51:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 09b2fa77-96ed-3354-885d-d4f1237ef87b | -22.78584 | -43.75703 | 2024-10-17 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24f75b38-1cf4-3918-bf39-0f03df895158 | -20.90217 | -43.81975 | 2024-10-17 03:51:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 538b270b-1a23-3352-85b9-41d9d282a9f3 | -20.25419 | -43.56305 | 2024-10-17 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c1095e1-0b70-3ee6-b69c-33d93a4cb6f2 | -20.25056 | -43.56207 | 2024-10-17 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0fe6f2d9-eda6-3cd4-a605-0013de7e7b59 | -21.61288 | -45.36446 | 2024-10-17 03:51:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a6a182b6-8e68-320e-b585-031cb0364564 | -21.61193 | -45.36307 | 2024-10-17 03:51:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 75ad7062-2642-303c-ab65-a5b61ec02f0c | -21.60998 | -45.35804 | 2024-10-17 03:51:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cac41dc6-daa1-3342-99fb-e91b555ba5c7 | -21.1809 | -44.27568 | 2024-10-17 03:51:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 728604fe-68f5-3f78-a2d2-7e4a089b31a6 | -21.00828 | -44.18053 | 2024-10-17 03:51:00 | NPP-375D | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c47dedd-c0d5-3dc9-b626-4487ace0f9a1 | -18.9334 | -46.30381 | 2024-10-17 03:51:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de47834d-2f4f-34e7-8e9c-130cdb63d4a9 | -18.93251 | -46.30845 | 2024-10-17 03:51:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7def1e41-5c17-3db9-881a-3e10fe5a7ec1 | -18.9324 | -46.30252 | 2024-10-17 03:51:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3907b22-50aa-3b30-bd1b-f66039b756a8 | -18.93149 | -46.30714 | 2024-10-17 03:51:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 968ff0b0-5fa8-3616-9cf8-e15bf0a3ee34 | -20.31182 | -45.58485 | 2024-10-17 03:51:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c31bd3-4249-3365-8bcf-a687e964064e | -19.6695 | -45.93958 | 2024-10-17 03:51:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56a6548c-a7b9-393f-9a57-f01e2bc2aba7 | -23.34635 | -46.18838 | 2024-10-17 03:51:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e449b75a-20f2-3d27-8e47-f64b3b599b54 | -23.34562 | -46.19212 | 2024-10-17 03:51:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8286b1a9-cae2-303e-9703-2062d932a372 | -23.34032 | -46.77309 | 2024-10-17 03:51:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c0749adf-1c35-3afb-9b2f-3e3ba772a325 | -23.16522 | -46.71275 | 2024-10-17 03:51:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6b2f2c85-d919-3dd0-9fdd-d6796660a8c7 | -23.00987 | -47.1809 | 2024-10-17 03:51:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae34078b-9cd7-3bec-8d38-2e44d208f42a | -23.00896 | -47.18539 | 2024-10-17 03:51:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a52cd20a-e3ea-333a-b554-f63817969d4d | -20.59164 | -47.55228 | 2024-10-17 03:51:00 | NPP-375D | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b114993-4a60-3d51-afe5-5ff4bbdadd20 | -20.4756 | -47.51832 | 2024-10-17 03:51:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e49dd24-6046-3622-82ac-4b3e57a9b8d3 | -19.69946 | -46.78701 | 2024-10-17 03:51:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 262f7dab-a691-345f-947f-b020fe8ee6d3 | -22.30481 | -48.33725 | 2024-10-17 03:51:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 360427d7-f97a-3104-885a-f11382d34e71 | -22.30012 | -48.33612 | 2024-10-17 03:51:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07896a9c-389f-3674-a4d5-ceda4973f20e | -22.60699 | -47.40362 | 2024-10-17 03:51:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6b16359-b43d-35dd-b274-c3821cfc1d8b | -23.36701 | -47.36762 | 2024-10-17 03:51:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cfa1efd8-cd9f-3881-aaf6-3cfcb8de0fb0 | -23.36269 | -47.36655 | 2024-10-17 03:51:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0d07f64e-17b6-3729-a2f3-660357c66932 | -22.94291 | -47.38058 | 2024-10-17 03:51:00 | NPP-375D | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e040935c-2d18-34f4-adf6-535891d08c1d | -25.19143 | -49.32931 | 2024-10-17 03:51:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7dc60e87-21db-384c-9406-aa3ec8a6562d | -22.54026 | -48.81487 | 2024-10-17 03:51:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f92a147-4c49-3ffa-9e10-04a880ba0997 | -20.1962 | -52.13882 | 2024-10-17 03:51:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3832a51-8471-310e-82af-3d63f6c65a5d | -20.19388 | -52.13874 | 2024-10-17 03:51:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb895a95-aa8d-3c4c-b9c0-bd19b8f4eef5 | -20.19017 | -52.13681 | 2024-10-17 03:51:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d342b8b0-9ffc-3d57-ad40-941b4d37ee73 | -20.99446 | -51.79418 | 2024-10-17 03:51:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e84f376a-86b7-350c-a7ec-2c51030568e9 | -2.9674 | -47.9931 | 2024-10-17 03:55:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| da77728f-d31f-3503-a9ac-24177591f29a | -3.7007 | -45.9223 | 2024-10-17 03:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 34a70f22-d4ee-3196-b61b-d2ab1acb1bdd | -3.7009 | -45.9 | 2024-10-17 03:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 45784908-b116-38c2-aac0-5e407d135cfa | -3.9078 | -42.4256 | 2024-10-17 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| a3b2af6e-06aa-3244-9321-a055f32e9e3a | -3.908 | -42.402 | 2024-10-17 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 198.0 |
| 5574a258-ec88-30eb-9a43-c0c7b610c7a1 | -3.9081 | -42.3784 | 2024-10-17 03:55:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 497523de-7847-343c-a0ab-0b8145eddb92 | -3.9265 | -42.4246 | 2024-10-17 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 01c55e11-7a06-3a8b-8278-fc1eabd2ee15 | -3.9267 | -42.401 | 2024-10-17 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 242.9 |
| 495b3d63-0bc2-3b82-99dc-6fba007ca16b | -3.9268 | -42.3773 | 2024-10-17 03:55:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 87f128b6-067c-3cf0-8a08-70bf121adb65 | -5.5716 | -44.8927 | 2024-10-17 03:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 567af1c4-8a4a-32eb-953c-7dc30bd1482f | -5.9788 | -45.3621 | 2024-10-17 03:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 984dda9d-d1c3-3f0a-97df-d9cf9322b5c3 | -7.8727 | -45.3593 | 2024-10-17 03:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fdf23576-70f9-34bd-92a4-f66b75003b2b | -9.1552 | -61.9047 | 2024-10-17 03:55:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| aa005e2c-7fe4-3423-89f0-a2d34b26e03f | -17.9036 | -57.4534 | 2024-10-17 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| fdf571f2-30a3-3049-97aa-39e39f06d183 | -17.8444 | -57.4607 | 2024-10-17 03:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| c8c7f3d1-88e3-3aab-8478-a1b1c221f96f | -17.8049 | -57.4655 | 2024-10-17 03:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 8e2986c8-5ca2-315a-95b7-ea9ae167bdec | -17.8052 | -57.4449 | 2024-10-17 03:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 0cced939-0c11-342a-8396-21bd7e8a6898 | -17.8246 | -57.4631 | 2024-10-17 03:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| e017ed54-b3b7-3a90-9498-01988a1dde50 | -17.8641 | -57.4583 | 2024-10-17 03:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| ba60fcd9-8141-3008-8c86-c01c2b38756b | -2.9674 | -47.9931 | 2024-10-17 04:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 988dc616-0819-32d6-9dd1-00bcb88b084d | -3.7007 | -45.9223 | 2024-10-17 04:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ee7306db-3291-37fe-b692-01670efa4fe8 | -3.9078 | -42.4256 | 2024-10-17 04:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| be6886f4-ea85-3293-9e0d-c3613d521408 | -3.908 | -42.402 | 2024-10-17 04:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 201.9 |
| b27c34c4-a8d0-33fd-a5f2-430965df39fb | -3.9081 | -42.3784 | 2024-10-17 04:05:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| a2a89e9a-140e-37d6-86d1-23d2fcde6f0e | -3.9265 | -42.4246 | 2024-10-17 04:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 148.9 |
| 95286c7a-a46f-34e7-9a6a-f70b1754074f | -3.9267 | -42.401 | 2024-10-17 04:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 358.9 |
| e0852da5-c593-3bda-989b-f87615dc68db | -3.9268 | -42.3773 | 2024-10-17 04:05:28 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| cde56ec0-c0e4-3d0b-8d20-a8c6fa80ff83 | -5.5716 | -44.8927 | 2024-10-17 04:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| a0fcd8ea-063f-3d49-bfa0-21b5e7f6cd02 | -5.9788 | -45.3621 | 2024-10-17 04:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 059c91b8-6310-3256-8d08-ede3df251782 | -9.1552 | -61.9047 | 2024-10-17 04:05:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 00564d12-df4d-3c30-863a-b0c983bd47c1 | -11.8624 | -64.9521 | 2024-10-17 04:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d9620293-ac5f-3c3c-b745-0ca21cc1ec85 | -3.52239 | -43.05924 | 2024-10-17 04:10:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1787475d-246a-39e2-9b65-dd6431af759a | -3.51821 | -43.23633 | 2024-10-17 04:10:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c368762-546e-3917-ae4c-6f93e5276e4e | -3.51766 | -43.23981 | 2024-10-17 04:10:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 546909c9-2d46-3545-854d-2ff7f258ebd2 | -3.29855 | -43.51025 | 2024-10-17 04:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c327a408-0503-3a4d-a421-4f199ff6c940 | -3.24554 | -43.02582 | 2024-10-17 04:10:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 224f787d-d9bf-332d-8e2c-ea4ab910701e | -3.71915 | -43.06143 | 2024-10-17 04:10:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a5721e-feda-32f2-84c4-cbf321049a8d | -3.12672 | -45.03983 | 2024-10-17 04:10:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89e3fa81-fd89-37ea-b59a-5ef925e30657 | -3.12609 | -45.04378 | 2024-10-17 04:10:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f222e246-4f70-3b97-bc83-bf132211958f | -2.86612 | -45.52136 | 2024-10-17 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb792c15-2e90-3fe5-8f28-31d44e721e7c | -2.32058 | -45.07453 | 2024-10-17 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 523723bd-ecba-3bbb-ae2d-496e8dd89405 | -2.31767 | -45.06993 | 2024-10-17 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b72df8c-2fd2-3f6f-896b-c82c9ef6f6a3 | -2.31702 | -45.07396 | 2024-10-17 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dfd8c33a-8ae5-3b7f-9311-caf22e96fc81 | -2.31411 | -45.06937 | 2024-10-17 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e25ea99-4426-3948-ae6c-c42939b9947f | -1.61927 | -47.08743 | 2024-10-17 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)

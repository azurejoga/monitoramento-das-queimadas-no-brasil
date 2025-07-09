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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e73d3ba-db1b-33b5-b172-314b6ee3311b | -7.0894 | -43.459 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d62de48f-b132-30d7-b2a5-b314091ef1d3 | -11.43455 | -45.11764 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dc7fa30-f8cd-344a-bc40-ddae28705894 | -6.94277 | -43.02953 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b46f82f-000d-3709-8433-a9025b938692 | -8.51344 | -43.29616 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 200b497e-91fe-31dd-9526-a68f444a5ca8 | -8.37619 | -43.94359 | 2025-07-09 04:21:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afe33b7f-8a52-3900-bc82-aaff11c0e85d | -10.57654 | -49.12119 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2bc273d7-68a2-352d-ba57-23f35e192a95 | -11.43344 | -45.12473 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbb93ce8-956f-3f99-8ae5-581a2971891b | -8.7617 | -47.66921 | 2025-07-09 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5603270d-f68d-3133-8099-7ac693c58a19 | -6.67821 | -46.30444 | 2025-07-09 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cd8ca31-4375-307d-8f92-09a004ae1838 | -7.64487 | -45.35379 | 2025-07-09 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9da88c82-f146-3281-8500-442f2fd351ed | -7.09329 | -49.16577 | 2025-07-09 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 116d7549-14ed-3b43-a7eb-5d71bec8cd2e | -6.85667 | -42.79605 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d09fc0d-878d-3d9f-b48b-f0c876be41f7 | -11.42287 | -45.10487 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3983ded4-8f0e-3632-aac6-76acecfe550a | -11.45585 | -45.10637 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad5a3f6-a0f8-32b8-b978-0aeed4ee949b | -11.42455 | -45.11604 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9628b87-5c13-3ca6-9db9-c78871a0a975 | -10.57871 | -49.1306 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8c5d35f-6de5-313a-bed2-8544ef2b86a7 | -8.50314 | -43.2716 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 3f5c467a-0850-3b57-9246-b2745592058f | -8.50486 | -43.28337 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| ff3f89e2-0885-3160-b06d-8473cdd433ad | -8.51229 | -43.28067 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| d9734092-56e1-3829-a280-e33431e2c597 | -5.58997 | -52.08186 | 2025-07-09 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b3e6c5-23ba-3720-8a32-f84569018aae | -9.41107 | -58.91335 | 2025-07-09 04:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 520e2c34-b48d-35b4-8f5f-0dbc4ff4a83c | -11.44415 | -45.09358 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25be3396-0fd6-3f85-ab99-8c7af50eacf4 | -11.44031 | -45.11844 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d2b44575-f11a-34f4-b2c5-b51bea9892fc | -6.95977 | -43.25739 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 1448b76f-0b84-3e26-a4e7-9944af3bc63d | -6.8492 | -42.7988 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96f4b202-756e-387b-b4d5-15e5f3ba4f17 | -10.57361 | -49.11625 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 919f9a31-9871-30ed-b14c-ac541ea31110 | -8.96919 | -49.85349 | 2025-07-09 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff377d4-f0d0-34e1-a19f-abfafee3dc80 | -6.88192 | -42.79232 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72819f88-6817-3cb0-9ef5-9083120a419f | -8.58579 | -49.87197 | 2025-07-09 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf8c85c2-d016-3659-8b23-d207b44d7de1 | -11.90443 | -44.91327 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96f06e71-a055-377a-b081-3f8b4b5e805f | -11.43976 | -45.12199 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 558d0d3f-c3c5-341e-92fa-5854d6ae4de7 | -7.36453 | -43.19122 | 2025-07-09 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 094ad35c-4076-3e40-9060-0a1bcefa51f4 | -5.96126 | -44.18718 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7120853b-d094-34c5-8a8f-cd3f61f98c67 | -6.72156 | -43.71687 | 2025-07-09 04:21:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a92bdfd-99e3-3cf1-9a95-fe877727386a | -7.08861 | -49.16275 | 2025-07-09 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1540f419-5dd8-36b5-8dd6-d049356a26f3 | -6.72892 | -44.33946 | 2025-07-09 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10bad4dd-df03-396d-973b-2ab802dfd7a8 | -6.83449 | -43.34608 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 118479fd-bb11-3c58-9e42-f974c0853064 | -11.43972 | -45.10015 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 696830fe-27f4-31ca-ac16-e6d79cb62fac | -11.42008 | -45.1008 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cba4eaf-c46b-3161-aa2a-ec09111d5bb1 | -6.56718 | -48.24192 | 2025-07-09 04:21:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff3de9fe-51a1-36e9-a0b3-c146b47dd766 | -11.42898 | -45.10948 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 96e2f7ca-045b-324f-bd76-f0b09178095b | -11.41231 | -45.10682 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e0c0b2-2e99-3911-8710-d289b5cfb155 | -6.72947 | -44.33598 | 2025-07-09 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a2e69c5-7ff2-35b9-a96e-1d82d3141fff | -8.50886 | -43.28015 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 3daacdaa-aceb-3569-8ba3-3f5e3f3b3cd8 | -8.506 | -43.27588 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 258f7e35-d602-3e77-be61-cecf54031c1c | -10.46099 | -47.94424 | 2025-07-09 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b2d3b81-0067-35e2-8e57-a0a43f17a587 | -10.56918 | -49.12 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eb0cab8-c4bf-32c8-9f4d-4a4f8f5315c9 | -8.50944 | -43.29937 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 4116015b-bae1-3f5d-80d2-eab9e41b587a | -8.04398 | -47.02127 | 2025-07-09 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee7905b-d31d-36c9-9564-b8e6a3453aae | -10.57211 | -49.13134 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03984db0-9f23-3214-9bef-5b76d3874cec | -6.14369 | -43.97308 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8124c90f-f30b-35fd-bab5-35098c80386f | -10.63434 | -49.45869 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fecc7900-eb4b-3782-b971-863acb331bda | -10.94986 | -48.1561 | 2025-07-09 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8d165f74-da06-3601-88b5-69be3c40a27b | -7.67641 | -44.35952 | 2025-07-09 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 669beed4-9f92-333a-b1a0-70733f4a2ab2 | -11.67831 | -43.78102 | 2025-07-09 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b5ab0e0a-2380-398b-8eb1-3839584f91ff | -10.63729 | -49.46387 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c4ac88e-f3cf-34e9-a67e-37b40ddd7be7 | -9.41233 | -58.91386 | 2025-07-09 04:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| befd8da8-5752-3d94-bbf7-285e8bad92c2 | -8.22198 | -44.93574 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90bf2d5c-6ff9-349a-8d2d-ff2de68690cb | -6.81354 | -44.77243 | 2025-07-09 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe9692e2-b6c1-3808-83b4-ffb93d08ae50 | -11.43399 | -45.12119 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb8ea98-72fa-3a4e-8b04-de74ca5679ab | -10.58314 | -49.12681 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c16c31d-082d-30fb-9ceb-bb14ccd1447c | -5.7816 | -43.60756 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 338bbdb6-5329-3d7e-a296-7ae4104575e9 | -10.57059 | -49.13381 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 507bda75-adb0-37f8-a2bf-5c6d0be59282 | -6.84466 | -43.35089 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c845a66-cdb1-3751-962e-5e7f531a51a3 | -5.95902 | -44.17972 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38f78b3b-570e-3f23-a1d4-82334f897f41 | -10.57284 | -49.12694 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7247bde-b03b-3754-a8fe-8a2f27aaedc9 | -9.01277 | -49.59817 | 2025-07-09 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edbe114f-7866-30a7-8231-5a1550385294 | -9.41378 | -58.90651 | 2025-07-09 04:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 202bcb7a-ffeb-3857-8dd3-867b2105dfab | -6.97938 | -43.38261 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4499952d-6893-3180-8075-a14f3b1c1b1b | -11.44309 | -45.12252 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c0a62f7d-8cb2-3012-9c8b-22c3ba83ac24 | -6.17296 | -48.04991 | 2025-07-09 04:21:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4a3a8ad0-5830-3322-977e-cd56cf4e7052 | -11.4553 | -45.10992 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6da3242-fd73-3b9b-83d5-ebd2127d8c28 | -9.79187 | -47.75011 | 2025-07-09 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3bdfff9e-76dc-3aea-a749-e5c868c26cfe | -11.47207 | -47.92364 | 2025-07-09 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7544afd5-de68-310e-9eab-1d84ca489bb1 | -11.43066 | -45.12065 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9db0e08b-6c26-349c-be9f-249a994abc7c | -8.7604 | -47.67702 | 2025-07-09 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa6a32e4-bb67-328a-9517-a2bc2d1b0f51 | -10.57357 | -49.12252 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05e65834-bb3a-329b-8865-8e5a22a7ea31 | -6.87018 | -44.06456 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46bde980-f6a0-3b11-a723-76e2892e53bf | -11.10903 | -48.86898 | 2025-07-09 04:21:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff7377c0-3010-3e66-b144-98ea72664bd6 | -13.40258 | -47.87843 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e55f9cb-fecb-3a1d-9981-35697ce77975 | -12.98686 | -44.87447 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43b42c76-8542-3952-96cf-4fd76a36dab0 | -13.3955 | -47.90014 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b80dd5b0-83e2-33b7-8353-1f2418d6e97a | -17.09337 | -43.8036 | 2025-07-09 04:23:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f9af9e2-3b2b-39e0-a22f-ed4da3ee0559 | -15.61455 | -46.45905 | 2025-07-09 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e5a7466-358c-3468-bb38-17ffd2bb1909 | -11.33201 | -55.21769 | 2025-07-09 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a7d30f-b7f8-310b-a8a0-044e91a8fcbb | -13.40291 | -47.89754 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5ebc4cd-fd48-3d0c-8de2-1c82898a8788 | -13.39918 | -47.87787 | 2025-07-09 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dcb6e2f-1de8-30c3-ad87-1c212ed7bbab | -11.33136 | -55.22106 | 2025-07-09 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5339be7-fd66-3caa-ab6f-b4068cb0498e | -13.01945 | -46.2897 | 2025-07-09 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b140de82-f976-3f68-acaf-8c010d280c84 | -17.26508 | -49.00721 | 2025-07-09 04:23:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11fdc302-2952-378d-b55f-94b50f8f7e4a | -12.9818 | -44.8849 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 757e78c9-705d-30eb-aa1a-b432242ea37b | -14.94786 | -42.35828 | 2025-07-09 04:23:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d54bf777-0ef3-31bb-9538-8db62c9dc50f | -12.98293 | -44.87758 | 2025-07-09 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bf21121-4584-3cb5-8d9b-0cc3b68279d8 | -13.63516 | -44.41645 | 2025-07-09 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23db8ccd-d2ca-36fb-bb09-90894f4b9db7 | -15.78841 | -48.25136 | 2025-07-09 04:23:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64a86a3b-7437-3e9f-9801-03dd26852e77 | -12.97316 | -47.83133 | 2025-07-09 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 767a60d4-8a20-3893-913f-c9b05d9366ab | -17.69164 | -46.75311 | 2025-07-09 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b11b3338-6519-3e49-97d7-7433c37c3ae3 | -10.30086 | -57.12543 | 2025-07-09 04:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 390a16d9-4077-3530-830a-ccac52c05f0a | -12.0513 | -48.54788 | 2025-07-09 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 196a2e04-f36e-3eb4-9ed6-68dacc2c67c9 | -13.70261 | -45.62078 | 2025-07-09 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README17.md)

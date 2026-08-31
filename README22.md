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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da2553f2-e5ec-365e-8428-efbac83b367b | -15.19532 | -46.24758 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96a4f536-0d4e-339d-838a-6364403fca63 | -11.20602 | -43.37572 | 2026-08-31 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f51f17e6-2c9c-3f94-9354-df02043eaf30 | -13.48144 | -42.47914 | 2026-08-31 03:55:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17040a7c-da4c-37fd-b025-c610b6219176 | -11.32653 | -45.19512 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e69ebf2-b0a5-387a-b891-a803b0cca95c | -11.37007 | -45.21935 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fadbb9b-d6ce-3766-9e26-dc81d68c1465 | -11.49291 | -46.9334 | 2026-08-31 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66658d83-18c1-344c-aec5-1a70ededf8c0 | -12.07655 | -44.98639 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 084cb4f1-086f-398d-b4be-413de82b3ee7 | -12.92514 | -45.86225 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9080290-8ed8-3d79-ae70-474bedcea1d6 | -12.91619 | -45.90795 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2c3594f2-b836-34b3-b847-54318fa14abb | -15.66049 | -45.91677 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2411cbce-a8be-383f-b66a-c423e3457e2c | -11.21116 | -45.09618 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d63171f3-beea-3ec1-a0a8-bb118e0ccb84 | -11.92819 | -45.06487 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2a6e7d0-341c-3f2f-923f-eb43529334dc | -11.34541 | -45.20833 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eda01888-7f64-3e8e-92ba-3c4aa6b37b03 | -15.0252 | -48.16665 | 2026-08-31 03:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 06c4a8a6-34f1-3244-bf47-b9e2c62dc4fd | -10.80603 | -50.65723 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dedc31ae-1289-3cc5-8729-eefd6640a7d3 | -9.42563 | -45.65216 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 133210e7-520c-3ab4-ba8c-4484100ace91 | -14.20231 | -46.56155 | 2026-08-31 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1af6f731-645c-3374-bf09-7554bd5e7a91 | -10.83833 | -45.32281 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80712f77-bea9-3d08-a2cc-14e3a48a7e1a | -11.93066 | -45.05181 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae38977a-af6c-3055-8e21-2e745a860d1a | -11.21855 | -45.11322 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 633a449e-87ae-3252-be90-a3edf3de0968 | -9.4373 | -45.68114 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87718869-4207-32df-b56e-d5fda2c3e78c | -11.7852 | -47.67072 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 413c9df3-b707-356d-b1f9-8010f7085797 | -11.67743 | -47.61041 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a75a199b-388e-3809-b6a8-90cd15281b20 | -11.21819 | -45.14303 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dfd78f1-a0ea-377b-9e61-4d616a4e9fbb | -12.89676 | -45.84627 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31cf4277-f922-30c4-b664-bc4231a11b49 | -11.34709 | -45.1994 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 046a8d70-1b92-3a12-baa8-41e9eb9222e0 | -11.24115 | -45.13447 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab5bc660-6a55-36bb-b0b3-2f1086dcd00b | -17.52898 | -40.24337 | 2026-08-31 03:55:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| faf33280-3761-37e7-8c75-3dea0acd0d49 | -12.92578 | -45.85895 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b813b92a-0f15-3079-a2d1-f20e809c216d | -11.24177 | -45.13118 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cc0b4e1-7941-33e5-8906-1d6ed0f755f5 | -14.19295 | -45.30441 | 2026-08-31 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb1b8532-d893-3f5a-8977-72c355079c0d | -10.75008 | -44.87787 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2a933e2-d9a4-3e81-a40b-e88eb99bfe05 | -10.74047 | -47.96672 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c5b1301-b2af-3f38-ace6-b6a72ee082f8 | -11.20882 | -43.38617 | 2026-08-31 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 21992318-6517-37f3-878b-0579a21075dc | -12.07603 | -44.98919 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b46dd74-a3e0-3c5a-a38a-43e2cb3ef79e | -12.10204 | -45.03828 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1d41fb3-cb2e-3ca8-bb40-14bd866292c8 | -11.20193 | -43.37818 | 2026-08-31 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ec1ac2fa-d5fa-3911-bddb-076c9b488538 | -17.79543 | -39.7059 | 2026-08-31 03:55:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6b789c5a-e29b-327c-b60b-b9f465486d77 | -11.23604 | -45.13334 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27712ec2-0417-32e0-b2b4-36899a593bf7 | -10.01374 | -46.3957 | 2026-08-31 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f965d6c5-3aae-34e5-aaeb-c6b304ff74e3 | -12.08167 | -44.98684 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81bc6f1c-4081-39d7-b273-e425ec65e4ae | -15.67176 | -45.93885 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2829e30a-9aa5-3588-9cfb-ec8a9196e94b | -15.70768 | -39.89702 | 2026-08-31 03:55:00 | NPP-375D | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00c242fc-145b-313d-9cdd-99ad1f79f908 | -10.7396 | -47.97101 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 616f1e69-5860-362f-be55-809cb04b0d64 | -12.13756 | -45.83928 | 2026-08-31 03:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99cc76ce-9e87-3e42-a075-43ea2eb2406d | -11.21976 | -45.1069 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5019d09-be30-3f49-8e8c-2c66a4d35ae0 | -12.38933 | -46.45158 | 2026-08-31 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbff84bf-f04f-351d-917f-4c44ab95dbac | -11.9271 | -45.07069 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72aadfbd-52b6-3135-bc69-8ffd03ceb5b1 | -11.35742 | -45.22974 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3554c795-7a66-3e6b-824c-7adcc4ec2eb7 | -11.68548 | -47.60912 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| edda9c94-36f1-30be-8854-524f1d687dec | -10.44448 | -46.76366 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3443b477-32aa-3cea-8a51-3c6fa388f1e0 | -13.19436 | -44.07331 | 2026-08-31 03:55:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a19b69ed-e56c-38a7-8cd7-3aa71503466e | -14.19188 | -45.30988 | 2026-08-31 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47264641-01bd-3d56-a758-b678da7f2138 | -11.3614 | -45.20854 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95708d69-c4b0-32d5-9ab5-7adcb9bf9aff | -10.75245 | -44.86525 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083fee99-8a64-3be1-a1e3-6bbbef874f1c | -13.38439 | -41.3296 | 2026-08-31 03:55:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 2331f8e9-d4b8-33ae-bea9-9b575900818b | -10.85512 | -45.37733 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88df87e8-c6b8-30e6-b6f0-528b658efc67 | -11.21212 | -45.119 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 879f395f-1671-3c8d-89b0-0e1bbaeccc7b | -12.94364 | -45.90695 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 113ea68c-d811-3f4a-8b69-8c4181f1093c | -10.79883 | -50.65561 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 11d32341-53ca-3fcf-bfb9-5fde8f94d7dd | -11.49269 | -50.3278 | 2026-08-31 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bad02380-76c0-350f-ab30-a1eca76f46ea | -13.38522 | -41.32481 | 2026-08-31 03:55:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 255ad508-f2a2-3053-9043-24ec7f8c1917 | -11.20562 | -45.05917 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e2dd43-ed44-38ae-9b1c-6aa1380c9c56 | -11.3695 | -45.2224 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4015b28d-e607-3c6a-a864-a2082584a6c2 | -10.84985 | -45.37635 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67574e75-8a13-32d5-9756-8b5a3cb0897f | -12.43563 | -42.89634 | 2026-08-31 03:55:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e619b67f-c73e-3f18-ab77-db3f6ee0a786 | -10.82973 | -45.31101 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e45c10f7-7020-36ca-b6f0-dea3cbfd06fb | -15.19395 | -46.25055 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4b47655-f767-3808-9a08-6b8da782ae9d | -11.6864 | -47.60458 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c69593f-824f-3230-935d-5f4e5b49b578 | -11.33111 | -45.19915 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f528c4c-04ad-331f-8220-902bff0b9c85 | -10.14782 | -45.69551 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dca19a1d-8c7a-33c2-8c0c-8f4ed275a167 | -11.2424 | -45.12786 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8c0592b-6926-3884-ae8b-42cd380208f6 | -10.73278 | -50.64158 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d89d3447-1bbe-3ceb-b2b9-46dc4cbebd61 | -10.75461 | -44.88195 | 2026-08-31 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4b80142-1098-3db4-b7c9-c4b93e74c5b9 | -11.33165 | -45.19633 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12f6157c-4a37-3e65-ac82-23f250b68bfc | -12.08667 | -44.9879 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 328df57a-a750-3b5c-9fe0-c8de895eec16 | -11.35855 | -45.22371 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bb3b5c9-e65a-3256-a408-9d33aa4b2f65 | -9.80502 | -46.45535 | 2026-08-31 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 60057d64-bfb2-34be-b691-c70843328b13 | -10.15588 | -45.74225 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30ea3670-d792-3b7e-acd4-e1b5ff864a61 | -11.22149 | -45.09783 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e270e62-e729-3854-a66f-2d12a234504d | -11.79209 | -47.66731 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b453bd7-e156-3f41-a2fe-ea7d7702e93a | -12.78413 | -46.4634 | 2026-08-31 03:55:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76722b9c-d0ae-38cc-9c54-5db8db50b6a8 | -11.21517 | -45.10305 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ce4eea7-66e3-36f7-a1cf-8ca2dd265b05 | -13.88502 | -41.63454 | 2026-08-31 03:55:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e199992-f8f5-3db9-bea1-6fd70ffdbf64 | -11.33815 | -45.16207 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0e2f10b-b7dc-351d-9f79-b90eddf4486c | -11.16017 | -45.04685 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07eab52e-9f3a-35b6-bdfc-899e9c276bdc | -11.22035 | -45.1038 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab39517f-898f-35b5-b2fc-067c81f86293 | -10.14565 | -45.70691 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f97461cc-f105-3e7d-ba8e-e51b5ea27e60 | -12.90216 | -45.84095 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57d2ae8a-71ea-3d7b-acd7-d6516ee8d483 | -11.21746 | -45.09108 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc0182f8-b84e-3c5c-95b2-3f19f20ff550 | -15.66174 | -45.9104 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0426f6ed-6ec4-32f8-b193-e2d7cecda71a | -11.37585 | -45.21699 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b7ab789-29f9-3ba3-b933-4ab246e23fff | -11.366 | -45.21252 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 084b05de-410d-3cb8-b6ba-8d1eb4ef916c | -15.19076 | -46.2395 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d1043df-9b10-34e4-9a43-73a85aa92040 | -10.80613 | -50.65915 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 611b0117-b41d-3d91-b4a9-11b129a578b3 | -16.28744 | -42.57428 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c619aae7-083b-36ff-ba37-633528b6d866 | -12.89634 | -45.8429 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b96820e-2428-3ae9-8384-e34ba306676d | -11.1653 | -45.04781 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de7d562b-878e-360f-bedd-01fb83da8ec0 | -10.73521 | -47.96081 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 439c7ad7-ec9b-3c64-81f2-0e4ebe7e5fed | -15.63118 | -50.09493 | 2026-08-31 03:55:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README23.md)

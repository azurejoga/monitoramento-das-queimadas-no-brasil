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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 428b4da8-920c-35d1-8fe1-b28c783b4191 | -12.86093 | -52.94565 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ed0dafb-8bf2-3d89-bbfe-d30aee5f1cbb | -15.19809 | -44.0444 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e47abda8-751c-3e62-abd9-09e5a7097cd3 | -9.98519 | -48.37965 | 2025-09-11 04:23:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84e36843-1dec-342b-8b6d-4647dd7a8eb6 | -12.84486 | -47.96672 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d49846e-55d1-3df8-a250-4a4c1f1ba196 | -13.8459 | -47.3557 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b26be87e-7fce-3466-aed7-cc6e46bfb6fa | -14.13243 | -45.40162 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d540b634-9618-30e3-b92e-4a4402e76899 | -12.03327 | -47.54468 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cd72d92-e1ca-33ee-9e01-7803a8d5376b | -15.12471 | -47.02746 | 2025-09-11 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f15e151-e488-3334-8591-abe92d61b045 | -13.84867 | -47.3599 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00f14bf7-1dd5-3fa0-9e5b-7ce30dad0aa1 | -9.59066 | -48.06789 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b0d1450-df83-3e8e-84c3-d42737353725 | -10.93922 | -46.79473 | 2025-09-11 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b2758fa-f280-3d22-b0a5-3522a8890876 | -13.84767 | -47.34483 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c54e030-f44a-36e5-97f9-ff939782bb80 | -13.16357 | -45.28562 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5bfb0b30-287f-314e-9355-9ed385147c7c | -8.87274 | -51.03587 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e74b715-df9a-3b0e-a55a-79339a53a9d2 | -12.96441 | -54.74842 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86ae4f35-2e75-36d7-8f57-1a67574e4125 | -12.41722 | -44.72639 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4b8fe27-545d-33f0-9db5-1d44a77acd87 | -10.93468 | -46.80141 | 2025-09-11 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 948dd157-474a-38c4-8d7c-63a1360b9b8b | -11.16655 | -45.27879 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5f84b9d-7d54-3473-bc19-e02871509c97 | -9.07785 | -46.96388 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6324b913-1ee8-3c7c-9eb6-8c47c5c1ee21 | -10.55682 | -49.88688 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b7df69e-373d-3778-90f9-a5f5d735d5be | -14.47293 | -46.35821 | 2025-09-11 04:23:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e95d68a4-60af-3f1d-8f98-de92aad62473 | -13.89651 | -47.98799 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a47f827-5899-3c0b-a0c8-569cda21f853 | -11.37672 | -45.57963 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bf81065-94f8-3284-9cca-23a5c0678784 | -10.00199 | -51.72063 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35d56848-512e-39b3-81e2-18906e39ddf2 | -10.14797 | -46.17896 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c6529e1-e379-3716-826c-f55f54d5317e | -11.49713 | -43.66469 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84f8526f-ef70-3065-a434-ad14e392652e | -13.16077 | -45.28148 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2f8d7966-96b3-33f8-8f0a-550eaadb9a79 | -15.24699 | -44.03122 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1356bb8c-a4f5-30c2-99ae-e91d743bbec1 | -11.46982 | -43.69269 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ae27ec6-4a33-3cef-b1e7-04cd8876ae82 | -11.34904 | -46.5022 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 086ef47d-e2ef-3d5f-9a56-170e5e36c090 | -12.82375 | -52.94142 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cec523e3-fbf7-3a45-b77e-855ee67bcdc1 | -12.53304 | -45.33625 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e35d4852-d9d5-3eba-a90d-a7efa7278721 | -11.09714 | -48.44947 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 122d6254-496c-338e-a7d6-c049c355fab7 | -12.93441 | -54.75401 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caa3f5c4-98a1-3793-81ed-de4ce1e2f2f8 | -12.95184 | -54.74522 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3511bbd-7fe4-322f-b581-888c589e6ff4 | -11.16159 | -45.31052 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9e9b80c-f994-3d01-b0b8-3a20a6ef53f8 | -9.064 | -47.04916 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ba0344b-eba0-3f36-bdcb-b8b5f39a2ea9 | -11.41781 | -43.56649 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b5a0043-5a3f-3889-953a-469433b95fa7 | -13.15296 | -45.28759 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bfe0181-5bd3-3038-aa8f-32ad090b1abf | -11.77618 | -46.51729 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2fa557ae-fa72-3510-a791-2a00db7a2448 | -12.00958 | -47.58263 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 300053ca-61a8-370b-a29a-e5733b7ff7e4 | -13.32458 | -46.37463 | 2025-09-11 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bba01223-b29d-3ace-820b-a7c0f6f523cf | -10.55297 | -49.8862 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bd8d714f-b2d2-37d9-a3bd-bcb7d6ca32ae | -12.58451 | -44.79026 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e53f8a07-201b-39f2-8eff-55ef3aca629c | -11.80474 | -46.75631 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9847125-d199-3490-8561-68a79911c7d7 | -13.64803 | -44.26308 | 2025-09-11 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20d81e65-f77f-39e0-9b84-d33e70504dd6 | -11.40085 | -45.59481 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcd59356-bac1-3123-8d74-b38687a7c935 | -11.76681 | -46.49023 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77270104-a1d5-3c50-8c06-d50e42f475ce | -11.48726 | -43.63555 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e7f4cbe-156f-3104-8179-44a3170fac8b | -11.40563 | -43.55266 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aac910a2-03ff-3eec-9427-23f32bf445ec | -11.7157 | -48.24797 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f921702-f605-3de4-b750-92174e2b8fe7 | -14.3833 | -47.34224 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 086e931c-f4ec-367b-9c50-02d006e36d58 | -9.68783 | -46.75424 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d5c1b12-b3ed-3977-aa4e-32af534c5cec | -10.14307 | -46.31641 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4241b45-71ab-34cc-9fb7-1f7e32834276 | -11.49333 | -50.57187 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 685cbef9-3253-319c-b37d-b32791a54935 | -9.08648 | -47.08407 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf4cfe1f-c27b-37b9-b055-a6c5622f0d87 | -9.30211 | -46.76619 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9bb875e6-6a26-3a43-a9b5-874286749794 | -9.99912 | -51.71137 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62e3b41b-166c-3a37-a209-e5c90992a28f | -12.24259 | -47.3335 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 961a6969-4720-3405-b478-372efd7d1314 | -12.142 | -44.85532 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbc7aee9-5c9b-3ccd-b31f-44fc622eb059 | -9.12476 | -46.19213 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23f80adf-96b9-3ccf-a0dc-a6fd0a23aa8a | -11.48502 | -43.67458 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 803450c9-434c-30d9-a256-2a62f78ce349 | -11.47339 | -43.62254 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b005e79e-6633-38e6-ad5d-34a0477ec836 | -11.38081 | -43.52213 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b59b032-bf01-3a64-a17d-2608a7ed83e5 | -12.04805 | -47.60448 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36c73499-ad7a-354c-af82-1b667aee35d1 | -12.97805 | -46.74025 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56425dab-9348-3d43-b920-b8bf5736314a | -11.39516 | -43.52719 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad5cacd9-5675-3e9e-8849-e16f3ec51c61 | -12.43087 | -47.80608 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9efd551e-7772-32bd-98a5-e657957c37cb | -12.30814 | -42.10394 | 2025-09-11 04:23:00 | NPP-375D | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3aa1032-1477-37d1-bd7e-7549d0f158fd | -13.24748 | -43.79326 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e10c097-489d-3cad-9a6c-f591779abafd | -11.39356 | -43.53205 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41b4cad9-95a2-38d9-99f3-86da40022676 | -11.74721 | -46.52708 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e97bb816-549f-320b-b23a-03d67b624285 | -12.93412 | -54.79556 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a5bb5c8-6a26-30ea-8c66-212db24ea57d | -12.13305 | -44.86866 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffb52ce1-258e-3b3e-abd6-ded730127c5c | -9.78588 | -51.1022 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ae4e05b-7e23-317e-98db-4819c497e3f5 | -9.89452 | -50.16771 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b83b5cca-0f2d-307e-9548-cf203b640f05 | -9.71962 | -48.09198 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2159b4b0-1d0e-3d6a-89f1-ed988486ec10 | -13.92912 | -48.23278 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8473ce5-6e60-3d98-b16f-92a5ba86bf71 | -10.0056 | -51.72568 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa5cf574-7616-3663-8a58-40eafd3c0612 | -10.56553 | -51.51457 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70e4ee35-5aa3-3508-8b76-fdaf3847fadc | -9.83924 | -47.78332 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b6f66d9-1397-3384-a364-b35804a99af5 | -9.01995 | -49.7787 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8e83514-25a4-3795-ac28-66d2063d30df | -10.10363 | -48.17335 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 210dc956-ffc3-3e1c-baeb-062426f055cb | -9.20674 | -51.8103 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5979c2b7-30e0-3a8d-9942-dc4a6306fece | -11.47105 | -43.63794 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9b8d2bb-5368-304d-9ef6-2f7928f4fc65 | -12.96772 | -54.75848 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64c7219d-3592-340d-a077-8f9e8d392d34 | -14.41413 | -47.32166 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4f5bfc4d-68e6-3d1a-bf0b-39fff5d1b0ce | -12.03728 | -47.54154 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a63c76d8-948f-3153-9934-bf7a62f9a50a | -13.24865 | -43.78535 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8e4b229-76ef-332d-b50e-80df82643049 | -12.03047 | -47.54039 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2553bad7-4413-3537-9a0d-0f4afc5f53f0 | -9.05958 | -46.96845 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8912e33e-db1b-3f4e-a7af-13ef1d50e414 | -13.9891 | -48.23231 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 745c4114-f3b7-309e-9a44-1bccecca4f0f | -11.39279 | -45.58585 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2a0471f-4883-37e8-93b6-b6278eea595d | -9.08023 | -47.07921 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f245ad04-13a4-35db-a6d3-53680222b453 | -11.10138 | -48.44589 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 464806cb-0fbc-3865-bf0f-19448ebb0a56 | -14.90705 | -42.80391 | 2025-09-11 04:23:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7009155-f007-3a65-86a6-784985635f22 | -10.02229 | -51.73319 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61d6c310-f26a-3e40-8c24-8901c58ddb57 | -9.5955 | -48.06051 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ee4dd0c-ce0b-306b-95ca-5e291df9594d | -14.41298 | -47.32877 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5511991e-3d36-3bc0-9fb1-563f87d0c1fa | -11.1939 | -48.41099 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README69.md)

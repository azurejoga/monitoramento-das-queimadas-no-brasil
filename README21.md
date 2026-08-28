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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a728803-9f21-3a53-bbcc-ffb6cbc39eb3 | -10.88935 | -50.5214 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| edac2899-bf61-3c48-8132-a1ed17133f9c | -11.23543 | -54.00963 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b44740a2-7109-38ff-9005-4d44ef3e9d91 | -14.87374 | -52.59298 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1a4a0d58-c343-386a-9896-de342671fe59 | -10.53177 | -43.98082 | 2026-08-28 04:17:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca814cfc-d2ce-30f3-a0a5-22d511d5ff8a | -11.7333 | -54.528 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e991c3c7-48a3-3b05-ab28-127195cbab95 | -14.17335 | -52.8238 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c2577eec-08c2-3b36-9283-17231ef07adb | -9.61658 | -55.11576 | 2026-08-28 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 715fb701-d945-333d-948a-9e66f1340914 | -10.32297 | -49.97707 | 2026-08-28 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a6d0554-9286-3d2f-8743-2df746c769ea | -11.19739 | -51.2395 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 80c39eb1-e52f-3a8d-a558-9a4de16150c5 | -11.20645 | -51.24115 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c87bcd56-d8c0-3c90-82af-3d0099f2485c | -8.80734 | -50.07689 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9cdd698-c7a4-3458-893c-971a2bf2e4bd | -22.69886 | -47.29319 | 2026-08-28 04:17:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf86e194-883f-3d77-ab24-642d09ee04f1 | -11.78058 | -47.64904 | 2026-08-28 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a955fe60-f93b-3437-a2e6-480ed0de5d92 | -10.91031 | -50.52953 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3148519e-f9bd-3c64-beba-ba9e7ee6f63b | -11.02049 | -45.07001 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12c58bbc-289c-3bad-91d4-822a33a336f6 | -12.01999 | -47.17006 | 2026-08-28 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 330c51f6-3249-367a-a843-bc8ad3e17f2f | -8.80728 | -50.08118 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6bd316c-89ff-3c4b-9d2e-0fa70f72d7ab | -11.5375 | -45.51641 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99f6ddc4-56a7-3bd7-a69f-be8bf03a6f0c | -10.96636 | -50.29876 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff316205-4df1-349e-96e8-4a0011cc4dff | -11.57151 | -45.51826 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c3fc728-2f44-38da-824e-614dd91692f4 | -14.18769 | -52.82641 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c2fb4583-31f9-3d16-b4a7-045c3abb86e5 | -14.39843 | -50.13099 | 2026-08-28 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c06453a1-e8df-374b-9071-105a2daf600b | -8.6004 | -54.79045 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a1d1799d-46b2-3a1b-8a3b-df77d6b465e3 | -9.15964 | -49.9719 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7488e973-f448-3005-b91c-00ac96fa8e5c | -12.78382 | -46.4471 | 2026-08-28 04:17:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e058a02-a791-3e32-8fca-06bbf827908d | -14.19093 | -52.83464 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f99a70ce-afba-3ad0-a830-60b999a9b7f3 | -11.57647 | -45.53012 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac624ffa-583c-31db-8d60-5796dd449d2b | -12.42643 | -43.41251 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ec62b4b9-847d-32e5-ba8c-0838311134e5 | -14.9939 | -52.60878 | 2026-08-28 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae24ce22-937e-33d2-a78e-f8edb96c9498 | -8.81027 | -50.08612 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eb25950-6152-38b4-99f7-a6eb3365f4f7 | -14.16857 | -52.82292 | 2026-08-28 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d5d78ed0-ffc5-38a8-862b-67292523c6ae | -11.23175 | -45.04601 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 891a11a1-ab03-3b49-b6ce-5664f2781e2f | -11.57265 | -45.51111 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88a90e66-3029-369e-abf3-cd750b7a7877 | -11.71414 | -47.79982 | 2026-08-28 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cc352dd-c77f-36d0-a92c-27968fcffe62 | -10.94607 | -49.59 | 2026-08-28 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91e3c1f3-4599-37a1-b339-219238cbc688 | -14.60562 | -47.9786 | 2026-08-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fdb4b8e6-811a-38fd-a9d3-855a7db7e0b9 | -12.27576 | -50.59919 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77bb659c-ec36-3ccf-9215-719affec3095 | -14.45294 | -53.35032 | 2026-08-28 04:17:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27cc6a6d-9556-3179-8c92-c167af4015d1 | -9.16254 | -49.96809 | 2026-08-28 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0c5c800-6e80-3f29-805e-2b80e6c2784a | -14.90976 | -43.41373 | 2026-08-28 04:17:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b5bb7de-919e-3d25-a036-0ee5c27e5db7 | -10.55656 | -50.4825 | 2026-08-28 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2d50a6a-15cf-3e69-aef6-be2965bb0f82 | -12.42307 | -43.41198 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aecbf158-24d1-33e0-ab84-5ba2efaaa4b6 | -10.76168 | -53.97982 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c200522-fd54-3e9a-9688-80765b58c3d5 | -11.24085 | -54.00339 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b8547f5-c292-3969-804c-2b550f6e5e5c | -8.60224 | -54.71385 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9dbedb7-554c-39a9-9ca8-39b823ecffa9 | -11.71851 | -54.54459 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a69c7f35-c3a0-3274-9b3d-3eb2920c8218 | -8.80804 | -50.07694 | 2026-08-28 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 134b049d-4db6-3f53-8394-6138af60be63 | -14.49505 | -53.40377 | 2026-08-28 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4543d866-6f1f-3281-9ca0-0323169de7cd | -10.17502 | -48.46738 | 2026-08-28 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24ca7fea-88e5-36fc-ad7c-214c74c51bdb | -11.7522 | -54.51986 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7867686-a227-39e9-b76b-86668a8317cd | -11.54199 | -45.50978 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 783b31d9-59f3-3293-a498-5161fc4f7464 | -12.28994 | -43.12757 | 2026-08-28 04:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cd1fe829-d698-3f02-a6c9-0dbdf3c31291 | -13.40834 | -51.41129 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| a449c01f-0d8d-39e8-a865-a2b980392638 | -10.03012 | -46.40212 | 2026-08-28 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6966726d-bd1f-3879-bbb3-8066235a73a0 | -11.72965 | -54.5468 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6896a4f9-d5a6-315e-ae00-08c9a7dea922 | -15.14953 | -43.79832 | 2026-08-28 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 719acca1-32d8-3705-99ca-b42372881c29 | -11.72702 | -54.53058 | 2026-08-28 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e883cf54-328f-3adc-aaf6-cf9893f72787 | -13.83955 | -54.04098 | 2026-08-28 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd60e4ba-8523-3b7d-8dc5-38dfa5082b52 | -11.65571 | -46.7333 | 2026-08-28 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 09848235-64e1-3e55-bfa2-61fed5e114ed | -11.81472 | -47.20562 | 2026-08-28 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb0fb5c0-eeb7-3f30-909b-5a6b63ef4608 | -11.22397 | -54.00341 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94afee8b-b8be-3b0b-9eeb-2546c9163ec1 | -14.96238 | -52.59756 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 715f6906-6d27-3d53-ac35-2d1fe4b404cd | -11.20833 | -53.9968 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d325bf4-4aa9-366b-a772-be665df0f998 | -11.2434 | -45.03701 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19109e36-391d-3667-87e9-24d1ced2745d | -14.89231 | -52.59652 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b919c48a-8a60-3d4f-84b3-2662d5b0869c | -12.71975 | -43.2046 | 2026-08-28 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47cf149a-d5ef-3d6e-b0be-cd140963bd34 | -10.84011 | -50.52131 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a45525fa-56aa-3b07-bd99-fd95a5bc2aa8 | -10.96708 | -50.2947 | 2026-08-28 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7bde6da-88d0-379c-8f96-2b58ed7abcc8 | -10.98879 | -51.0864 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c164fda-ab20-3b29-a433-2aa76d290453 | -11.70978 | -47.80346 | 2026-08-28 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfffa1d5-b3f7-3563-81a9-85cf312eff6a | -21.32231 | -45.93076 | 2026-08-28 04:17:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6336491f-58c9-3f34-beb4-806bae6acdb8 | -14.87739 | -52.59919 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2bb6af02-3c0d-39bb-a4b9-6d05bb8ba708 | -12.76161 | -44.26633 | 2026-08-28 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f7dacd7b-687e-32ac-b15a-2408cca664da | -15.60073 | -46.57865 | 2026-08-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 16cbeeb8-fce2-3ac0-b909-8076c4e04323 | -12.50861 | -43.81166 | 2026-08-28 04:17:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d1eee717-b140-3e0f-ae83-3e407259fe73 | -12.29056 | -43.14638 | 2026-08-28 04:17:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6fbf986f-905b-3dfe-ae93-788eeda87996 | -9.97327 | -53.93608 | 2026-08-28 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 63554d79-f4e8-3d3e-a075-11636324c0b8 | -13.99063 | -41.20571 | 2026-08-28 04:17:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f12e200a-a353-31df-bb20-4f5882c624bf | -14.39972 | -50.12378 | 2026-08-28 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d6e5db4-28d2-362b-92b0-1a2b8fc81db9 | -8.60818 | -54.71494 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e583887-b4e1-333b-af9b-2a7a08a7e221 | -14.60914 | -47.97936 | 2026-08-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5777a73-d450-38b6-98c0-79a0ac97fd98 | -11.2253 | -53.9963 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9661596a-bada-31ae-99c8-a3c8ea9b5e3c | -15.82139 | -48.09444 | 2026-08-28 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ed050740-427b-36ea-8353-7d9710457860 | -10.7973 | -54.00132 | 2026-08-28 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2c2796c-e6dd-3f48-acaf-a523ea29262c | -8.158 | -54.95848 | 2026-08-28 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38e9c46f-8de0-36ae-ab83-e31eb898117e | -10.17362 | -48.46473 | 2026-08-28 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b49b57b-0a7c-3410-83f0-56de64fcac6f | -12.42978 | -43.41303 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 8e29de1e-a08d-3f3c-8713-7d4633cf8df5 | -11.19369 | -51.23402 | 2026-08-28 04:17:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| be4deafe-0ebe-3215-8921-4f25a08a7e94 | -10.56985 | -57.48738 | 2026-08-28 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e059400-e687-3aca-8d6b-0eeb210356f8 | -14.86057 | -52.61197 | 2026-08-28 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cfe73780-abf7-3fa7-b8a0-213e72e29892 | -13.60515 | -45.78048 | 2026-08-28 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fef71539-9ebd-3bd7-9f3b-5b0153808915 | -12.42697 | -43.4089 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 253b0d0a-3ee6-3b9f-8492-cd6b063836ab | -13.41032 | -51.42536 | 2026-08-28 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6eacae12-d737-3672-9626-c42256c9a462 | -12.20983 | -50.57458 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6487dcc8-6118-3023-9751-27ddf84f25f1 | -14.11987 | -44.38246 | 2026-08-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61ef126-827f-39ad-a03e-3b7bde8bfac7 | -12.43032 | -43.40942 | 2026-08-28 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 482f2f72-b4cb-3ade-a570-74c501d64981 | -11.57474 | -45.54088 | 2026-08-28 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0c966cc-c490-38c7-86a2-c0cd2de190c9 | -12.28002 | -50.59997 | 2026-08-28 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7d18127-16c8-3643-b3ea-93febb6b1ca0 | -9.65938 | -48.30017 | 2026-08-28 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06e16a14-c1a2-3259-a789-5226df62c806 | -13.45884 | -54.01875 | 2026-08-28 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)

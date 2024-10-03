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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de84684-7051-3ef5-8fc9-a83696047428 | -14.69697 | -48.76105 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fb58e651-fd53-38ce-9fd3-4705bad32006 | -14.69647 | -48.7649 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e965420-96d7-349e-ab21-d09136b8e342 | -14.6939 | -48.75177 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5e82fbdc-c711-38ba-887e-ee76318fc5f0 | -14.69333 | -48.75618 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92e9e7c5-3f5d-3a2a-879f-8aa7dcd570f8 | -14.69283 | -48.76007 | 2024-10-03 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d7ad282-75e5-3b7c-a665-2ddee2884dcd | -14.49945 | -49.28437 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d38ec1de-f6ec-3cdf-86e8-3e9f85e52387 | -14.49911 | -49.2869 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 23cf00df-a1d2-367a-b3ee-a1ba02d7f58f | -14.49891 | -49.28822 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34d5c9f3-07d8-37a4-8d14-c53c1f604b50 | -14.49541 | -49.28372 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6aed6ba5-a472-33c0-8496-c165ddd21066 | -14.49508 | -49.28622 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 528218a3-6d45-3cc3-ad34-ec3ec79a4ca5 | -14.49488 | -49.28752 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 592c92d0-d9fd-3da1-ad26-b6d4e9d353d9 | -14.49139 | -49.28296 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0203544-2d8a-33f0-8362-8a43441f381b | -14.49087 | -49.28674 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00314ff1-9fa8-3f32-9727-350898781182 | -14.48684 | -49.28604 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fc6c0a3-a2a1-31d6-a3ec-e1e236e0a0ba | -14.48632 | -49.28983 | 2024-10-03 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12491062-3983-3169-8974-ceadb81ad5fd | -15.59656 | -48.77758 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f902387e-7038-39cd-9bb0-ae33d8c6a10b | -15.59598 | -48.78203 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 48f61b02-559d-377e-99f0-8c2ac399a02b | -15.59232 | -48.77695 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3bd07339-3754-315c-863d-fbfc1da03afb | -15.59173 | -48.78151 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 86c60ebd-1c5f-3b03-92a5-df452017a227 | -7.85994 | -49.65414 | 2024-10-03 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6466e78c-450b-303a-bf63-accf5dc8091d | -9.1018 | -49.78193 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3075ebc1-0c46-34e1-bf9f-4303ebf5b9be | -9.03999 | -49.82077 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9332f80-48df-3510-b0b1-04b13d487d7d | -9.03744 | -49.81798 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27b2d7d7-f337-3c84-98d5-b08e49eb6d63 | -9.03695 | -49.81595 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ff85da7-521d-3a80-aafa-9949731e29b9 | -9.03077 | -49.81263 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8634d154-cc49-325b-bd9c-c93e73bbda8b | -9.02712 | -49.81207 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bf65283-a936-3589-bde2-218d09acf49d | -9.02648 | -49.81633 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d7fa368-3a20-3962-ae76-5d2812c8091f | -9.02346 | -49.81151 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a7b49bf-9b76-3396-b869-ba71a884786d | -8.95052 | -49.74797 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0c4e571-52a0-3699-b6d9-af705f5c777b | -8.92023 | -49.67818 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a613977-3f81-3252-a296-1724a42c0eb2 | -8.87623 | -49.64497 | 2024-10-03 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c9dce82-cfa7-3027-9ade-0b4abd3a4074 | -8.85365 | -48.93898 | 2024-10-03 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca5e5042-ee31-3599-aa48-627ebef2a68d | -8.85155 | -48.9405 | 2024-10-03 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f3c6adb-4516-3c95-b9a7-ea73c021633a | -8.75233 | -49.78244 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 62b6dfeb-59cd-358c-b829-a805fc94f6ce | -8.7517 | -49.7867 | 2024-10-03 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d050c96-39b5-3237-ac12-f576bbfc57b1 | -8.26151 | -49.35014 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d6402a7-7237-37bc-914b-2d92a4f1df44 | -8.24894 | -49.38439 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b007f3fa-c6cb-32cf-8fad-ecbeb5794ac7 | -8.24777 | -49.38207 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34f7990e-b348-30d5-9c3c-a01605a647f5 | -8.24211 | -49.7615 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2eeda31-2992-3dc0-907f-d12e7adb0c54 | -8.24148 | -49.76573 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c077189f-5fdc-37e3-843b-c03de874e494 | -8.23848 | -49.76096 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc21884b-46cd-3269-86ce-5de35b29cd9c | -8.23785 | -49.76519 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50fc02c4-061c-3d0f-97ff-06a4e661be94 | -8.08728 | -49.52863 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e243ecb4-2838-340d-a676-934bea933cfa | -8.08621 | -49.51076 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d45be6f8-1adc-3483-8202-9f44d9109c17 | -8.0836 | -49.52816 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7450848-f1db-3476-be09-1286ef50732c | -8.08254 | -49.51022 | 2024-10-03 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5365de6e-606d-3f34-a331-283c186d8217 | -10.51322 | -49.79322 | 2024-10-03 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b7425bb-4046-3981-90b8-3238d54596a2 | -10.5001 | -50.26069 | 2024-10-03 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 869df926-9317-3261-8135-0724fd4dd9ef | -9.88654 | -50.13522 | 2024-10-03 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17a1a1aa-8fc5-3fdf-9b44-1bb49d4e390f | -9.88592 | -50.13945 | 2024-10-03 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 796040ae-e7cb-37f5-9499-4cd8db753211 | -9.82382 | -49.60913 | 2024-10-03 04:51:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d77239c-39a6-3d40-9c98-9e81bdf3a6a9 | -9.82152 | -49.60737 | 2024-10-03 04:51:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae3277f7-6868-345e-8bb6-8e5dec6d5395 | -9.62648 | -50.10922 | 2024-10-03 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cab5b01e-447d-333c-bac5-f6831f7c8642 | -9.59711 | -50.18194 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79118b65-ee56-3dab-b796-0f5086481a13 | -9.59649 | -50.18612 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38d5e9f6-6edc-31bf-b765-66a47a7a6d02 | -9.59587 | -50.19028 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31972f9d-eb3b-3533-ac5d-c55d2fa28491 | -9.59524 | -50.19445 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72646681-9e02-393b-85b0-ea604c14e29f | -9.5935 | -50.1814 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539fdb42-a76e-3bb7-8ccd-c4734e55d0c4 | -9.59288 | -50.18557 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69f64cd8-67cd-3bde-ba3a-2bb0adcf194a | -9.58565 | -50.18449 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdff2bcb-7602-395b-b0c6-33bb24405114 | -9.58503 | -50.18866 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dc7d8ec-b2dc-3598-8729-9c42cd5eba3f | -9.58204 | -50.18394 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01091725-c1a9-3439-af9a-85c737f4b667 | -9.58142 | -50.18812 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74fbd2de-e9b4-3bf5-b9f1-fcb61f93947a | -9.57781 | -50.18757 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0488fb4-0b21-3660-8e75-6cd7b4c07c4d | -9.5771 | -50.21725 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bb776fc-2cd4-39d7-9924-29f7c257d6bf | -9.57288 | -50.22086 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 592bfd2b-e456-3e6b-b48c-01a42f7dbd8f | -9.56962 | -50.11784 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9233227-d50c-3eb6-977e-0af07d49c5b1 | -9.56928 | -50.22031 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e0b2be3-87ce-36b6-a9ed-f2540e4a8e10 | -9.5669 | -50.21145 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00443b81-7358-3f07-aa68-c02120760ead | -9.5633 | -50.21091 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab7d8080-60b1-3aab-86bd-efba93797562 | -9.55547 | -50.21397 | 2024-10-03 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d5bc72d-7d7c-3771-95cf-6a9e731a4a9a | -11.35188 | -50.78695 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 687755d1-98f3-36c7-9745-6325e85f63ac | -11.35066 | -50.79515 | 2024-10-03 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f0f57f5-10e8-3ea8-becf-8f1387811d2e | -12.18695 | -50.08508 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21c8910a-5034-3ae5-ae49-b429008b86b5 | -12.18028 | -50.05154 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4fa7691-5041-3b58-8990-8dcb8c500643 | -12.17588 | -50.05554 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aee85dfe-1880-3c0b-a651-3419a874d24d | -12.17523 | -50.06009 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 382a62d5-91e9-3cb5-b79d-5ef632532222 | -12.17459 | -50.06464 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d769dd99-6c47-3d16-88a6-78b781a9608a | -12.17408 | -50.45958 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4237388a-e84b-3375-b5d2-6c01f9f6fa23 | -12.17214 | -50.05498 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62681645-37e9-3675-8464-9454aa834a5e | -12.17149 | -50.05954 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c46d29f2-8c25-3887-81ac-7c7d05d370c7 | -12.17084 | -50.06408 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 369cd6a6-8a33-3bf5-9b9b-8c541b657ed2 | -12.16977 | -50.46337 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 123d5a65-ece0-31da-a32e-891fc0283a66 | -12.16913 | -50.46771 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c906ba4-fa2b-3e63-af49-dccf98cecaed | -12.16774 | -50.05898 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 999c4fbc-bb62-3f28-8947-525283e8b778 | -12.16464 | -50.05386 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 338d9722-541f-3347-9737-8a5c17a6293c | -12.16399 | -50.05842 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4617fb3e-face-323d-9533-2ba41cd4d456 | -12.16089 | -50.0533 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c161772-5aea-3205-a954-6d4203363e6f | -12.15715 | -50.05274 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22e446ce-5f20-3296-864e-5697d69d755e | -12.15404 | -50.04763 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62ad963c-b15d-3207-ab3b-7ed6e1559f93 | -12.15029 | -50.04707 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d534a2f-f3b7-317b-926b-3cecd4e2f5a8 | -12.10072 | -50.0141 | 2024-10-03 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de84bb1a-8f62-3256-add7-bba897b83265 | -12.00926 | -50.30726 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 404b7a0d-b998-3adc-9377-f61e899e9fd3 | -11.97586 | -50.18692 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c0ac783-c22d-30f3-897f-286436e01353 | -11.97345 | -50.17743 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69f7a0c2-0af7-3183-98e8-2b69bcf60725 | -11.9728 | -50.1819 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e962678b-fde1-31b9-af09-b407589e54ea | -11.96973 | -50.17688 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f61c648-82b9-30a1-8bea-bfbeb6199a12 | -11.95066 | -50.15123 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 08357e97-a20e-3572-9178-4bf95a828c35 | -11.94695 | -50.15068 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5eb101e3-6542-3805-ba96-a46000532c00 | -11.9463 | -50.15516 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README126.md)

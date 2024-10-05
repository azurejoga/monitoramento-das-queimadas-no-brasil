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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c1d17a-55dd-38fb-8197-cc4d4f7b8d76 | -8.39955 | -47.74003 | 2024-10-05 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f9a49bb-7814-3a60-923a-431519a02cfc | -8.39843 | -47.73752 | 2024-10-05 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 814f8634-0ee6-36cd-9aa2-c65092f83995 | -8.39726 | -46.30709 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b645a124-b0e0-31fc-a4db-d251251753a8 | -8.3966 | -46.31115 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48ac363c-9a8e-3d44-9181-73e0313dc6fd | -8.39593 | -46.31526 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b433ca4-86a7-39aa-bce6-96f0648cf848 | -8.39369 | -46.30654 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f628b13-eed7-3d8f-9389-aa0dfe2879d3 | -8.39303 | -46.31059 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b87a3d5a-a13b-3f4c-b072-0087a04d326b | -8.19574 | -47.64154 | 2024-10-05 04:14:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9b06fd3-1d6e-3c44-a775-8f901eebe291 | -7.90655 | -54.75333 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c07ca287-7607-335c-84a6-b71ed8615335 | -7.90584 | -54.74924 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d13eaf38-f054-37b5-87cf-bd1fa77fb28e | -7.90569 | -54.75802 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b4e6352-2e2b-37b9-b04f-ce7053e2e64f | -7.90496 | -54.75385 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92b5f1a8-11ad-3115-abb8-5dda8d4b4743 | -7.90483 | -54.76274 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4f4420e-a476-32b2-a28e-5fe3bdc5a401 | -7.90407 | -54.75854 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0880c5c5-0023-3255-8b6f-529ca12c1a5a | -7.90317 | -54.76326 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 336cc356-2b0a-3564-bbf9-00ec9f719b3a | -7.90041 | -54.75211 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3858942-59d7-3f05-bbcd-713b71f35be4 | -7.89972 | -54.74798 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1beafe39-0a0e-379e-ba8f-4e67a2fb2cb8 | -7.89882 | -54.75269 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7367bdd0-c708-305f-b0a9-9e36f7dea487 | -7.89869 | -54.7615 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13d8dabe-4321-39e0-ad67-e456640efd2a | -7.89703 | -54.76205 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b99cae9-582f-38e9-83f7-e613ebfa4721 | -7.89516 | -54.74608 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da56fdf6-2b5c-330d-b39f-8f0b44419df7 | -7.89428 | -54.75087 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d856b869-5c6a-34cd-9c4c-5db40130a458 | -7.8936 | -54.74667 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f52cd689-e312-37ad-904c-c2decf747b7a | -7.88271 | -54.88354 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cce5518-9bad-3b0a-b0e6-6562ab257656 | -7.88112 | -54.87904 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f06eb2b6-eb5d-331b-91f8-3d626a679e76 | -7.88021 | -54.88381 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73fea203-78ad-37d0-b331-c3dbe6df5570 | -7.87929 | -54.88866 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fb37f78-8cc0-3361-a936-68a2914ccbb1 | -7.87829 | -54.87269 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1067a52-c76c-3019-9a7f-e911a3ede66d | -7.87739 | -54.87756 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8eb911a6-0b3d-392b-9da8-9cbfbb2d9177 | -7.87651 | -54.88235 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88811391-6373-3add-9e76-528ab85e9f1b | -7.87585 | -54.87302 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4c1baa3-c519-3f47-b02b-a782af94b2b1 | -7.87563 | -54.88714 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e236cd1e-4d78-38ad-8d37-82e1f59471a6 | -7.87493 | -54.87786 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bb46b60-aa82-3ae9-aba7-3599aecb6e1b | -7.87401 | -54.88263 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8620b4b-1e02-3c01-9284-3c89df6b790e | -7.8721 | -54.87146 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0017f52-2bf8-30a6-a81b-18f52bfbd0fc | -7.8712 | -54.87636 | 2024-10-05 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 606582fa-2544-3714-9393-80fb42b40c3a | -7.81299 | -50.23538 | 2024-10-05 04:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ad2f5d9-e688-3253-9894-de66c5f50e9c | -7.75895 | -46.14918 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4945d278-2660-3d20-af44-49b01fb7222e | -7.75538 | -46.1486 | 2024-10-05 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0f011db-f245-35e3-a4a3-dfb21c8a345a | -7.75096 | -49.21397 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae65c109-86cd-3d81-9754-4f0a717a7a45 | -7.75026 | -49.21801 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98c68065-f4a9-3084-9334-4fdf52063f5b | -7.74599 | -49.21725 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 435d71e8-77d9-377e-91c2-004745eda480 | -7.74529 | -49.22128 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a693e354-018e-39f5-922f-e9530ba16df2 | -7.74171 | -49.21649 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c05f0ced-8d49-366c-b57e-2f26b6aa6959 | -7.74102 | -49.22052 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3d5e7da-0e5a-3408-a1d6-6318dbc00ec0 | -7.73744 | -49.21573 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c53fe57d-7cf3-3e73-827a-54e72df0a8e8 | -7.73674 | -49.21975 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2942febd-e6f7-383f-acb2-1b4fed9a03c9 | -7.73604 | -49.22379 | 2024-10-05 04:14:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0808323-b8eb-35b0-91a2-ccf35f9e6b0e | -7.62442 | -45.53443 | 2024-10-05 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76d417ff-de24-367e-9ab7-4a4480fb56e7 | -7.46702 | -47.17705 | 2024-10-05 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ede781-1b71-3127-afb9-e4635e3305ec | -7.46247 | -47.18103 | 2024-10-05 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9b5fed3-a11a-3f62-9990-48a6dac6e553 | -7.46171 | -47.18565 | 2024-10-05 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83dcc1a2-5622-3889-896a-24acbe247cb4 | -7.39512 | -47.12023 | 2024-10-05 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70deb83f-790e-3f6d-a17e-a03120a6fa4d | -7.37941 | -45.42472 | 2024-10-05 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcaff89c-fbcc-3104-b964-1f0ea9544c2a | -7.37393 | -47.2494 | 2024-10-05 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43fd05e8-4e49-34eb-9dde-318df0103f9f | -11.11429 | -46.51167 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e26380e-f236-3237-82b6-afe8f469e34f | -11.11363 | -46.51563 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a044b24-5c46-31cf-b499-b73adf2e74c2 | -11.11218 | -54.23233 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cc4e42f-6323-3794-9954-1071eca0ed04 | -11.11143 | -54.23628 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6406930-a281-3206-95b8-e330f75d91b9 | -11.10963 | -54.22889 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68c34dd3-b8bb-3eb8-8552-1c6828ce4587 | -11.10886 | -54.23284 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9de7fb3a-2beb-3f25-972a-9b8bc2838536 | -11.10808 | -54.23679 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1680ea3-7a5c-380f-af37-0c16499fa916 | -11.1073 | -54.22724 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fef0fbc-18f3-3d77-92e2-082a7875c249 | -11.10655 | -54.23118 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4951243-4fde-31f8-81d6-25de5cbaa336 | -11.10579 | -54.23516 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9af288e8-ed59-3219-ad89-3130b18e14c5 | -11.10505 | -54.2391 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a79686e2-8e6a-32e4-ade7-ccf5aea3707f | -11.10477 | -54.22387 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9d4f91a-56d6-31c8-a0e6-216f33e7d6c7 | -11.104 | -54.22779 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c84cce6a-9e11-36fa-a6b7-b6e28b7b494e | -11.10322 | -54.23175 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f436b08f-6ce9-3924-9246-77d06351f1b9 | -11.10165 | -54.2262 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93a176d2-a04a-3bcf-a1b4-2057899b5ac9 | -11.1009 | -54.23016 | 2024-10-05 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9da65f99-d081-3fc5-a70e-b16393f7aaf2 | -11.0817 | -49.61061 | 2024-10-05 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b83e714-4cd2-3345-8f26-6c60c491f1ba | -11.07754 | -49.60986 | 2024-10-05 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64452c49-208c-374f-a328-cdc65b5c3ec8 | -10.95762 | -49.58032 | 2024-10-05 04:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13564cb0-645f-317c-af68-0b51d19ef77f | -10.92143 | -46.67238 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d15c9c54-4a02-36d3-b5e8-c28bbe3f2428 | -10.9179 | -46.67178 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00c925a2-3a46-3b7a-b641-a4e166cc4bed | -10.91724 | -46.67577 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60cea32a-df58-3903-9c06-40ca9bb16f6e | -10.91371 | -46.67517 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7a0a240f-5562-3eb5-9238-8919b8bc7398 | -10.91018 | -46.67457 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cb7c0384-c3c5-3b2c-a3ce-5a08a023601e | -10.88927 | -52.396 | 2024-10-05 04:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b1ee2fd-9d93-3759-bbd3-4164c3029ba6 | -10.8882 | -52.40179 | 2024-10-05 04:14:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b87fe4ae-326d-34e3-b0a5-91e09249ab42 | -10.88791 | -46.63394 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d13265cd-e69e-313a-aeb2-ed40015ee2ed | -10.88487 | -46.60874 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5397ca95-b463-382f-9f40-25b411513df4 | -10.88438 | -46.63335 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efd8d8fc-a98f-3966-81da-f374f2dc0174 | -10.88287 | -46.62073 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d39ea29-629f-3da4-93eb-c16c1b3c225e | -10.87934 | -46.62015 | 2024-10-05 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df6b5adc-387b-3938-b46a-268bf53177f4 | -10.85131 | -48.12985 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 293fee6e-5b3b-3f53-acde-1add3cf6a554 | -10.8489 | -51.06506 | 2024-10-05 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00db8d4e-a450-3ded-9e57-e2f7fc14754f | -10.82028 | -50.10873 | 2024-10-05 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 085acb89-8a2b-3bbc-ba37-fd66a691f674 | -10.81953 | -50.11287 | 2024-10-05 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00def9fa-da84-34a2-b35a-9b9695800ca7 | -10.81671 | -50.10381 | 2024-10-05 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a156f4cd-82b4-3d97-b55b-b41d5d294951 | -10.81596 | -50.10795 | 2024-10-05 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e6e68a3e-f761-37ef-9a60-a22d1bd85e50 | -10.77774 | -47.9966 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 64c834df-1d01-36b1-800b-51f0d9e9b7fa | -10.76934 | -48.00023 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28f6062b-9804-3f47-bc8c-bc1a0f5609b8 | -10.76855 | -48.00485 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11a112ba-9afa-30c5-93d9-cb94b7f1859e | -10.7648 | -48.00399 | 2024-10-05 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa879071-1d15-3438-a569-a9035289084f | -10.74184 | -48.71552 | 2024-10-05 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c420534e-e671-397a-b588-b0d53c433079 | -10.74125 | -47.73092 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07d09c84-29b8-3e74-8b91-e99f185c464b | -10.73383 | -47.72941 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7415580c-50bc-346c-9a85-99c7d5c90b43 | -10.73013 | -47.72862 | 2024-10-05 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README68.md)

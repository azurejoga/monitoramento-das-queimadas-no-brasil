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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 739c0424-bd8b-33c9-b6b3-bc0dec1c0b6a | -8.54218 | -54.71946 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 829be0a3-0e97-324f-a4f8-8d22d380cf21 | -8.57953 | -54.74891 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1069bc94-7e76-3246-a625-19d290ca7f43 | -8.21863 | -55.02481 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c41a001e-b7b1-3bee-b620-e00ad3097e11 | -8.08133 | -61.3643 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48fdaa17-097a-34e5-85d3-daae167098b5 | -8.54509 | -54.75027 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d3175fd-87fe-30ee-8661-1c5bf84ea9ea | -9.21476 | -60.81458 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bc5e3aa-ac92-3a71-8e32-908ba264b233 | -8.58044 | -54.70862 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9866aee0-43fd-3748-afc0-32e1752199a8 | -5.49152 | -60.14201 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55cd55da-055d-351e-a35f-4f78c141e8c1 | -8.57722 | -54.76661 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e7fa9cb9-0b23-300d-a824-199bd1fe7568 | -7.05847 | -59.84806 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eaebffff-7f68-3b1f-8371-4f079b1e2004 | -8.57517 | -54.6956 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b11fcb2-269e-36a3-b8da-f5270b0dc4cb | -9.38762 | -60.55032 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ae8a89d-d8d5-3b45-9ff2-764b25af3972 | -6.85264 | -59.02245 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2963e168-d903-3e53-929a-3cb66799379d | -7.88783 | -61.1869 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 304dd3f0-917e-3852-91ae-21b25210eb31 | -8.19122 | -54.99707 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1be68476-c939-32b2-b4d2-135b56f01a9c | -5.49817 | -60.13707 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 186ec8e3-b112-310f-b347-1875c80b8a70 | -8.5819 | -54.75228 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 601a319f-a30d-3184-8a45-84333249ac34 | -8.56798 | -54.6791 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04ef2d47-e7ea-3c28-8d02-d0dd5822ff6d | -9.02108 | -60.49754 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6751207-51cd-39d7-9563-5c94b31b1fa9 | -6.09004 | -57.91643 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a5bcd448-495a-352d-acd9-7c0c5a34bae4 | -8.57798 | -54.76072 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f575fdce-ac58-3eea-8c6a-e2711d66b428 | -5.49882 | -60.13252 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a23a430-0ca2-31b4-bb2c-feadc38a1f0a | -9.40886 | -60.56816 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 686f9100-46ab-3e1f-a683-6ca9e11e359d | -6.75836 | -59.15159 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 845355c5-a35a-3763-aefb-d097a0f61c89 | -9.21019 | -60.81394 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a534d38e-f911-31a3-89da-43c5448aebe7 | -8.55879 | -54.77315 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5c249c4f-e6c7-3925-95ba-b9253ef7ad09 | -8.56552 | -54.77406 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a39702ec-25a0-3771-b832-9aaf44e06d72 | -6.68694 | -59.07719 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e088602-af58-3e26-86bd-11cc3a7cae7a | -5.4981 | -60.12908 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43e5152e-5be4-3b38-bdb5-be04ec863b94 | -9.38889 | -60.55667 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e37b92c4-ae6a-3fc2-8e6f-39e249b387bd | -6.34482 | -54.90395 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b2cabd9-18f5-3c10-9706-d99eb2f393a6 | -6.00246 | -57.85631 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 485a8f84-867e-3edf-b3f3-94b6d78f0c04 | -9.42218 | -60.45053 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d852b50-4259-3027-b4e0-38f619b28cd9 | -9.40426 | -60.58366 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd52773-5392-3178-97e1-6f2bcc30cd8b | -8.57047 | -54.7658 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c819d514-6ed7-3ee0-9328-cf140d70f2f8 | -8.5699 | -54.68247 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5a4f351-d8de-3d83-9206-d1db0bc4544b | -8.5488 | -54.77465 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 782f77ef-7d12-31fb-a787-fc904e481786 | -6.33971 | -54.898 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06223d23-6bbe-385a-9668-30bb87bbe90f | -6.34266 | -54.9202 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 098d5db8-5b9b-320d-a262-6b6088d7bc9a | -6.09145 | -57.90654 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89802b26-3bc5-35aa-abab-3863877bcf04 | -8.21934 | -55.01911 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7aa97ede-c696-386d-bb00-81d414ed2a3f | -6.75182 | -59.16216 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47182f83-b8a8-3878-b843-ed0ea63433af | -6.04142 | -57.7966 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fca54c58-b23b-3b1d-b3e9-4d99cb2334d8 | -8.95877 | -60.58498 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf50587c-1b09-3ce7-a91e-e23a13ee6f9c | -8.54741 | -54.73215 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 153b48ce-7b95-3057-879c-5f180903de34 | -6.69548 | -58.94662 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 289a47f0-d808-3132-8b9e-062a5d73a16c | -8.57236 | -54.69843 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6dc592a-a5b9-38c2-a777-fad4a38d9b27 | -9.11261 | -60.38927 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e7e6b29-240d-3630-9d52-c347eb4a9509 | -8.58263 | -54.74639 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f880fc04-5a6e-35d8-a2d6-164d8bfa77f4 | -8.58472 | -54.7616 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 47c48a93-87c9-3788-8c36-4d427547987d | -5.99714 | -57.85542 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6b95834-4c48-34f6-b052-20e38d719fef | -9.40223 | -60.56348 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d43c242-4112-36a7-b3f5-1eb01e0ce20e | -8.58317 | -54.7734 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 97516e36-005e-3370-8bcf-fb2d2a5a1b99 | -8.54894 | -54.72022 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cb5874d0-e258-349f-bf77-d4c62bb10db8 | -6.33835 | -54.90292 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16c23f1f-c8c4-34cf-8bbe-3ea01b5e1f84 | -8.56638 | -54.69147 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61c4170a-99e7-3976-88fc-3125a4f89747 | -9.4215 | -60.45554 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d7cc68-0205-3030-bf5e-5cb2bea1f6ee | -6.84736 | -58.99178 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| edd20f92-250e-3803-8ca0-c39e4cd8a74d | -9.41357 | -60.58501 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5df509d7-5e54-3ef6-b854-de30141bfdbf | -6.8878 | -59.06181 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1f1e23f-b1f1-3ae4-91a7-5eb1d23c8199 | -6.00148 | -57.86312 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ae55528-a9f7-3988-b0b1-56e0b9d60113 | -8.55931 | -54.74623 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fe8e82f3-978f-309f-91ef-1045f4b8bba4 | -8.5528 | -54.76622 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ef7db3cd-9905-385b-abfd-1983b1f39537 | -8.56446 | -54.7594 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 915853cf-21f0-3621-82c3-f4ff2053a4e9 | -8.57442 | -54.70171 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9193254-99cd-3629-84d5-221c361e2ad3 | -8.57315 | -54.69231 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51f08b12-6aeb-3b9f-89e0-8448a3e24c94 | -9.42572 | -60.44993 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afe60796-e8bd-3a6d-bcdc-4a4096853b46 | -7.05514 | -59.83742 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3d2f7de5-8cce-38ab-8fad-ef2eb54c3397 | -9.40282 | -60.57723 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7150a452-66e7-3377-9afb-0b067c2cf612 | -6.08957 | -57.91977 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9d4cea29-c216-3528-a4e7-0dd762d252e5 | -8.07702 | -61.36359 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8cb5eda-8fe4-3902-aed8-c93e8c075cd6 | -6.09098 | -57.90984 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88661a3e-24cb-3a6c-8c07-a1af97cd1f34 | -6.85685 | -59.02878 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5c62fae3-c323-3b05-8ac1-404b7a81daa0 | -6.63575 | -59.08127 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a7c983-3a85-3986-bafe-d54907758156 | -6.88603 | -59.0385 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7042f6d4-4568-3c95-ba3f-8af29ae4b663 | -6.70472 | -58.95345 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22a86ded-3bfa-357c-94e0-9a0d464e7b54 | -9.42281 | -60.41003 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c735cf28-fb9e-30db-a8f0-af55f7df925a | -4.47113 | -55.45867 | 2026-08-19 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6f4f463-9444-340b-9dee-12780a26a6bb | -8.57591 | -54.74532 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b4012b4-c9c8-3d86-b54e-009453db3fc6 | -9.22324 | -60.82054 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05aaa3ab-5011-3ca2-9c1a-9fd109d7a244 | -8.21721 | -55.03614 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97760de0-e7ef-3135-9160-b8d53988c2a2 | -6.81127 | -59.45993 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82cfe78a-4c1d-38cd-940d-27f40c0f251a | -8.54431 | -54.75628 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42ee8c8b-27ae-3171-b56e-fb33a69d8415 | -5.49357 | -60.12841 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f749d15c-e5a2-3ba6-a548-bbd8a242a819 | -6.79193 | -59.45696 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fc40577-ba6e-3383-9189-4b47aa2b6f57 | -8.53468 | -54.72448 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04feba91-a7bd-3c7c-a35d-9c871e0616d5 | -3.55392 | -62.0765 | 2026-08-19 05:59:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d994175-55c0-3bb1-92bf-e57d9fc930d6 | -6.99761 | -59.04382 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a10e1e-f8f0-3455-b1c5-3f391780cedc | -6.34554 | -54.89855 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 584c6c67-cb50-3c38-9e4c-387367e6cbf2 | -5.49741 | -60.13362 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19e75b86-17e1-31c6-8746-0e324f2d60cf | -6.04001 | -57.80684 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4564a474-d924-36a1-be81-fb75e60e87cd | -9.14063 | -60.61432 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 269ef4e2-cb10-3751-90f7-e1d0e14013a1 | -6.14302 | -57.86917 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8db738d1-a5d1-3a7c-97e3-5b7203d8d63d | -6.13748 | -57.88927 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 155097e7-0aa4-3973-87e0-f79b78b75f30 | -8.55774 | -54.75842 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 109858fe-12c4-3bdf-a42b-7dba9878d290 | -6.78373 | -59.44491 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbbe413c-a229-3393-9085-ff42782159e8 | -6.09858 | -57.85655 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78aa5591-2c80-3e8e-bde7-7c2ffd5777f8 | -7.04899 | -59.84687 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 342d3a80-ec53-3bf7-9a9f-37e5cb92718c | -5.4943 | -60.13184 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 259e474f-1347-3cd2-8357-91d4f2f6365d | -6.7566 | -59.46254 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README65.md)

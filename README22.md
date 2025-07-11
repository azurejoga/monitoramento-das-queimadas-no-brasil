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
| 287c5957-595f-37a2-8bb3-7d5cbeb67f8b | -12.09636 | -64.2509 | 2025-07-11 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1ab2c33-594f-3aaa-bd73-6e30b96235b9 | -10.67521 | -49.48497 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 97bfb465-4a20-3024-8eed-2daca3879f28 | -12.0181 | -49.52252 | 2025-07-11 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f64b7dbe-26d3-35c2-9d58-b90abb335a53 | -10.6804 | -49.49632 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 43642928-76b5-3b10-b2dd-398ccc8a547a | -11.57184 | -47.43431 | 2025-07-11 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8671362-2868-3a1a-8811-0da5f643388a | -10.68166 | -49.48568 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 407845ab-0f00-3b0f-b6bc-d48fac5dc594 | -11.87423 | -58.72128 | 2025-07-11 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7092ba68-44c5-3c50-9e9d-7f80d6449692 | -12.09351 | -64.24636 | 2025-07-11 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f47e3437-55dd-371e-9d31-1e8fc2497d84 | -11.78055 | -64.9852 | 2025-07-11 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56bafe5c-31d4-3507-b51f-6f81074d7dd6 | -11.83906 | -47.50336 | 2025-07-11 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a7b67d1-e3cc-3c78-9cac-20eae9777bdf | -10.5712 | -49.14722 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| db49d5ae-91e4-335e-b7b0-e7f26f5e3005 | -3.75176 | -47.11757 | 2025-07-11 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 785f9c52-4543-3435-be67-490c7f7c491b | -7.9267 | -61.55745 | 2025-07-11 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c781e74-598c-368a-965f-64d83f2888a4 | -8.3809 | -51.07244 | 2025-07-11 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c29fbea-f6ed-31f9-a232-4fca1e7314a2 | -9.95914 | -64.97044 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48da726a-7400-371f-97b8-e52236b9eedc | -9.92812 | -59.90267 | 2025-07-11 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e0e4c52-5d3f-3f9b-b2c8-ceed52c2a37a | -9.4729 | -57.32909 | 2025-07-11 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 977f2965-ab1d-336a-b579-053840a30a71 | -10.57191 | -49.14141 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 54ea921a-ba2e-3836-be9c-4b46309a61eb | -10.57914 | -49.13668 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c3727098-4e56-3c61-8265-f6be697b6e2d | -9.91249 | -47.83347 | 2025-07-11 05:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4da9a2ca-2c28-3bd1-bdf3-5c6c7ec54f9c | -10.56955 | -49.14634 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1f07b2d-5b1e-3152-ae25-f1911a7d9ad2 | -7.90176 | -61.52107 | 2025-07-11 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0748f46-b0c1-34e0-ae29-499248e207ef | -9.96584 | -64.95338 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b149ac6b-419f-315d-8eeb-d4b79637a072 | -9.9466 | -64.95463 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6bc25c2f-c567-3042-9470-22310318a7de | -3.75353 | -47.10535 | 2025-07-11 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad1ac82c-872f-365c-b848-3c31f4df1f4b | -9.61271 | -49.02122 | 2025-07-11 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39491f82-6e30-35dc-aa02-644fafab8a51 | -9.7191 | -61.2895 | 2025-07-11 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 559d605a-a705-38bf-a590-81112e113bd4 | -10.5798 | -49.13131 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c7f2e868-6999-3975-a2f3-b2927ee09d81 | -3.79024 | -47.09161 | 2025-07-11 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1643cc51-062c-346c-99d2-84d7c2704cb6 | -10.58457 | -49.13154 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 674af5e7-3fb4-30fe-b47d-e6b26fe89811 | -2.44538 | -47.47039 | 2025-07-11 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8470a4a7-9fa3-3bcc-b155-efc2ac858b4d | -6.63063 | -56.27619 | 2025-07-11 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd8d47c2-4286-30e1-a84c-db822341a398 | -10.85627 | -49.11813 | 2025-07-11 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3042bb6d-ded5-399a-a281-7356ff3cb9c2 | -9.90978 | -47.83254 | 2025-07-11 05:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3dc6f882-115f-326f-948e-3f6140944366 | -7.89251 | -61.4766 | 2025-07-11 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 357fb8a5-e1c7-38bd-a3d7-3bd7ee8d7d59 | -7.78099 | -61.36933 | 2025-07-11 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d8b0fcb-decd-34e3-b35c-4fa7bae5a35d | -11.84406 | -63.22884 | 2025-07-11 05:25:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8868798f-1a9c-35f6-8b25-d74d680a8726 | -9.94215 | -64.95841 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60f7425d-d2fc-3b94-8ef2-7268ad38a5db | -10.57865 | -49.12509 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76295341-3d16-3d6a-84e7-712634872bbd | -3.78341 | -47.09083 | 2025-07-11 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 568e1dc9-0aec-3587-95e4-ec888a6d0a32 | -10.13108 | -57.77645 | 2025-07-11 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f75cbbd-f69d-3dad-a291-0f6d1e3f9237 | -10.67996 | -49.48961 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a1bdbeaa-b192-3c19-9a23-14b4a7bf9e51 | -9.33427 | -58.85462 | 2025-07-11 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81af8913-fa17-350a-9289-ad748c244d3e | -10.13414 | -57.78145 | 2025-07-11 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9755a4d5-1bea-3f7d-8ac1-3385cf0cc837 | -11.87547 | -58.71293 | 2025-07-11 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2b1ad69-2b0b-39bb-a2e6-e8e48b8f0844 | -9.91053 | -47.82598 | 2025-07-11 05:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b25aebc5-dc78-3868-a1ae-6ff95e3f6f1e | -9.61926 | -49.0219 | 2025-07-11 05:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f28ab7c-5937-3837-8d3e-8634e4ab117b | -11.86073 | -62.73746 | 2025-07-11 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7b60f58-c8c3-3c2e-af49-0f1e0df33e50 | -10.11479 | -65.14918 | 2025-07-11 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ccf3667-b383-3593-8e24-1208b086368b | -9.96509 | -64.95779 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e93cfd4d-b2ae-394e-847c-495f5f029ddb | -13.00996 | -47.82579 | 2025-07-11 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0aa85840-1e88-3ca9-b501-3bd70880be8b | -12.054 | -48.54909 | 2025-07-11 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1d5094e-bc7b-3f7c-a1ae-9cd3702bcf62 | -9.86422 | -60.29518 | 2025-07-11 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a361feb-51ca-3bb7-af12-90ee32f26bf6 | -9.96214 | -64.95274 | 2025-07-11 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2692b32-aa24-397d-b77e-6d1a486c5cc7 | -12.09286 | -64.25029 | 2025-07-11 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b893a6f9-9d06-3d78-990e-9c492342829f | -11.88205 | -58.71824 | 2025-07-11 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb007115-9aea-3bfc-b46c-6f4dd25c3217 | -10.58046 | -49.12592 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e3b12547-44e9-3986-883f-0d71669d61b2 | -9.244 | -58.7622 | 2025-07-11 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d136f0-d220-31f2-a527-938fceedf416 | -10.68103 | -49.49099 | 2025-07-11 05:25:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d599c0fb-5f61-36e1-bbcb-4441c107aaed | -3.75265 | -47.11146 | 2025-07-11 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ceb66734-98c5-3cbb-bbb9-9eb0eec3bb77 | -12.097 | -64.24696 | 2025-07-11 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14aabc0a-200e-3346-bc07-b4cd680d9151 | -10.84311 | -49.11635 | 2025-07-11 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 668ba67f-6156-3fde-81e2-31838addd11b | -9.86483 | -47.87411 | 2025-07-11 05:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 631f9e17-e219-3c63-b4fc-fd0d2750ad2f | -10.13479 | -57.77703 | 2025-07-11 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5439ada-9ae4-3483-b1aa-b4471280e577 | -18.42653 | -54.55875 | 2025-07-11 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f86b8e1-72ff-39af-84c5-61b058b84258 | -15.50237 | -56.30982 | 2025-07-11 05:27:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd609e30-94f2-3ded-9f26-1cbc0f7aa423 | -21.5375 | -49.53043 | 2025-07-11 05:27:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 095c70f9-2035-3c52-9705-7a1aceb3c2f9 | -18.66045 | -55.7242 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 64f065f5-0ea2-372c-a39d-2fbfd875fc53 | -14.43138 | -58.72406 | 2025-07-11 05:27:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c17b35d6-92d9-3c8f-9b20-9a0ae81bbc5a | -14.43573 | -58.72015 | 2025-07-11 05:27:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42c2e91f-c338-3b37-b942-ab9e3da73d2a | -18.65155 | -55.71767 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0b6f44ea-beb5-3271-b133-7bba5226c816 | -19.0871 | -56.04462 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 98481447-1964-3db3-aaae-faedd28db218 | -18.42142 | -54.55799 | 2025-07-11 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19c3490a-61ca-3967-be9d-f92c6f82b787 | -18.97375 | -54.39005 | 2025-07-11 05:27:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d46e26b-08d9-3ef5-8957-136060f30b5a | -18.66521 | -55.72482 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b92f7c5b-6f64-3b6d-b74f-9264d02652a7 | -18.65095 | -55.72297 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2e2b3b88-3778-3643-ac4f-e6bd17e14c2e | -18.64973 | -55.73353 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bc4dfa3f-1c32-39c0-85bc-c763cb221ed1 | -21.68866 | -49.50167 | 2025-07-11 05:27:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 857e23ae-7359-3f38-a561-8a378835084a | -19.09178 | -56.04524 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8fa4066c-0b17-3175-94c7-d74c2a1c5964 | -19.08649 | -56.04974 | 2025-07-11 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 79f18d17-80e1-33f4-8bbe-694775f48fd5 | -18.97411 | -54.38685 | 2025-07-11 05:27:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8943acb-4c56-317a-9455-1f5b8463335b | -19.9746 | -54.34034 | 2025-07-11 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 817f7ebf-fd84-35b4-875c-9a23ee6bf274 | -19.97495 | -54.33694 | 2025-07-11 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| feeeb4f6-b42c-33d8-a0a9-5231add6d666 | -18.42463 | -54.55859 | 2025-07-11 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53ca294f-a049-39fd-b4c1-963b716b5c57 | -21.68914 | -49.49437 | 2025-07-11 05:27:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0c6fe82a-e984-3721-8da3-a0fc285e1137 | -20.70547 | -56.6635 | 2025-07-11 05:27:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6597696d-fe76-3b5b-a842-bcb3d3f7eb46 | -21.6864 | -49.4964 | 2025-07-11 05:27:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| acb063c7-15b0-3561-a93a-ee52226ed064 | -18.42974 | -54.55937 | 2025-07-11 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 724c7d0b-8295-3617-83d5-338fe675e466 | -22.28262 | -54.94609 | 2025-07-11 05:29:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 199e7543-67d1-3dd0-8754-9f19636764f8 | -22.28752 | -54.95008 | 2025-07-11 05:29:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a66c0534-5107-3d31-85e7-45d6225b6589 | -22.28228 | -54.94945 | 2025-07-11 05:29:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa908068-f5dd-3cfe-a15b-b2b9b8f90a6b | -10.6672 | -49.4895 | 2025-07-11 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 621e4345-3374-3777-a961-a2f03f53ed46 | -5.5427 | -43.9096 | 2025-07-11 05:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6a584dee-054a-3f77-8a51-280485dc0d4c | -5.5429 | -43.8864 | 2025-07-11 05:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| cd584242-b196-3216-ace2-ca32321c3902 | -10.6862 | -49.4874 | 2025-07-11 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b296c3fd-679b-3e5c-af44-7eb7040d0b80 | -5.5427 | -43.9096 | 2025-07-11 05:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 2a4a60e0-7287-38cb-9113-c5ad9477a084 | -5.5429 | -43.8864 | 2025-07-11 05:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7cd79f8f-c6b7-3797-b692-b06a923c8adb | -6.62753 | -56.27953 | 2025-07-11 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af8560bb-de30-322f-81f8-88153c201c67 | -7.78337 | -61.3673 | 2025-07-11 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34f06b17-b159-347b-a950-b009239a9c82 | -9.92602 | -59.9073 | 2025-07-11 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)

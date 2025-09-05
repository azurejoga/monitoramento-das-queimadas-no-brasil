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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88f26dfd-6b62-3209-b60f-f0ceb726c842 | -9.72413 | -51.02639 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47c6c8b4-f403-35b6-b26c-50e1be5578ad | -11.91586 | -46.64655 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00d0f243-00c7-3590-a980-8c8735ad3d72 | -8.92052 | -45.11569 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3ccfda6-6753-3535-89a3-6ce2f9f27e83 | -10.95965 | -45.96249 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 235d9aaa-ea8e-3246-8e63-d673fea94121 | -13.29289 | -46.84503 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fc34f69-0568-3cae-b4e1-aa7b43c3d4f7 | -8.04938 | -47.5635 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6e4955ea-d0dc-3d63-b8ac-fd7ae92197cb | -8.89531 | -45.76926 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ca08ac9-6ef5-35e2-bee9-4b906dd15385 | -8.99707 | -45.52502 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01f150af-1c10-3800-a9ed-a936155ce4ec | -12.51533 | -48.07791 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f74610b8-6dd3-3aca-95c9-809fa7502e44 | -12.29577 | -50.00522 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9f21997-559e-347d-90bc-3e0f9015f58f | -9.44619 | -46.81038 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be1cefb7-9f15-3654-9c0b-9350c74f80b1 | -7.69583 | -50.25892 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4760419-9256-3701-9b8b-44d94be7caa5 | -12.01971 | -43.78876 | 2025-09-05 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcf0e4e5-83ec-3638-839c-78769bf2fb60 | -12.832 | -44.45377 | 2025-09-05 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a3804f04-b1eb-30e1-929c-4e6657b10d53 | -13.65862 | -47.92056 | 2025-09-05 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bbe5d59-6577-3929-9efc-dd82862ca94f | -8.48345 | -45.0554 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9601300-9b6b-320c-856a-b781b6b2e967 | -10.97978 | -45.99906 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e75c31c-3889-3e46-9d42-ac21f559a94a | -11.9986 | -46.74657 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57b294c8-3a89-3438-87b1-077bf81e2fae | -11.64662 | -54.54099 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa93b29d-7cf3-370f-bc32-2af634cb3da3 | -8.19328 | -49.60408 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c8507f8-4107-32be-b45f-6731dc33f4c2 | -10.84948 | -47.27932 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53de118a-7a66-3659-931f-238d8a054d68 | -10.05993 | -58.39122 | 2025-09-05 04:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e598585-6f17-3608-846d-c6ed6bcfa32c | -10.47523 | -53.62173 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d6d7ae1-8aa3-3e4e-88b3-4b57bf72a9bb | -7.75469 | -48.78724 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0def2118-34af-3143-92eb-f3328992a346 | -7.72536 | -50.3185 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f8e84a0-c0e5-38fb-8337-8b8e756fd03f | -11.10426 | -52.0242 | 2025-09-05 04:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c675917-5411-3c09-9381-6c29a15e3dfd | -10.76354 | -45.27443 | 2025-09-05 04:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba794c57-ef19-3334-b2b3-20dafbccb789 | -8.48283 | -45.05956 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33d7ffd5-543e-359c-a485-d189382c44c4 | -7.77308 | -50.97304 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0aa237b-308f-375e-b49d-30bab181ccd6 | -10.07434 | -48.0562 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cc3cb83-d01e-33e3-8c83-512a7b7782b2 | -10.14424 | -55.16595 | 2025-09-05 04:36:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e65e15da-50d2-341d-96ab-1066894861a6 | -12.29403 | -50.01598 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbba1879-aab5-3cab-8316-6832ca7f2b4b | -9.79826 | -48.31114 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43f271e1-e8e5-30f2-a0ec-15f10b3728ae | -10.50933 | -57.77644 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3efcb77-4196-38a0-9a1a-39024948fe8f | -13.30398 | -46.8185 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a67abfce-72c6-3347-818b-97a317ac6679 | -11.64448 | -54.5288 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71787de1-c420-3905-a960-2c5ab3655a7a | -11.95002 | -58.72989 | 2025-09-05 04:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8175e51-addc-3fee-aea9-10d9bd2da5ed | -8.08821 | -45.33047 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad42acda-490e-38f0-850a-5aa7bf7ae2b3 | -8.6507 | -54.84717 | 2025-09-05 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afb792c4-b547-3173-87b1-246d627c7ddb | -11.55091 | -47.31876 | 2025-09-05 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a498490-6153-37d2-b0c6-33b104e0670d | -10.76722 | -47.74968 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 925674e3-01b8-305c-870e-8b5639c9a673 | -10.76967 | -48.28567 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d3c8661-9234-3d93-8153-a9b34b4464a5 | -9.57403 | -48.22909 | 2025-09-05 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f894453a-908f-30fd-b3aa-80a60bdacada | -9.97378 | -51.63387 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a9e8740-b54a-3fe5-951b-e53a8fa326cd | -5.505 | -60.13034 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fb660218-e555-3906-9d94-0bc3ca203c9a | -9.08227 | -46.99912 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bb6362dd-d3ae-3cd3-9e8a-ea8c650ac4d3 | -9.0738 | -47.0091 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 243ea03b-5d6f-3534-8266-4d302f04a065 | -10.76523 | -48.2922 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07a8cd50-e18d-308f-8d9f-6b26fb856c50 | -10.46723 | -53.62036 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a947cb0-6737-3d3e-b86c-625de2cc3f58 | -10.07444 | -48.71776 | 2025-09-05 04:36:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f6e798e-0e28-3ed4-8a44-c881548cf9e4 | -10.09547 | -48.07409 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b7ad715-85b6-3792-a593-cc5f932be5cc | -10.16488 | -46.25406 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a6f0415-add6-3b6d-8466-e24405070673 | -11.72916 | -47.75086 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a9be123-f06c-3ca8-8e77-6778c5efd462 | -12.29681 | -50.02012 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90a7d21c-f669-3962-9563-24ed0815b51f | -8.34473 | -48.305 | 2025-09-05 04:36:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 294abb29-c309-3eb4-b198-7fe9b48d184d | -10.07324 | -48.06327 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41cfa623-8303-3632-9dee-8e1206eb064e | -9.83158 | -47.81489 | 2025-09-05 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96319da0-6881-391a-8747-9ed971eb6cbe | -12.98608 | -48.05822 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27e0b988-0c60-3fdf-bcd3-25c230ca4f2d | -9.07325 | -47.0127 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52eea09f-ffc9-3b41-887b-8f10652ffb28 | -12.48362 | -53.83494 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 396780d4-65b1-37a0-b5d4-c067f75c8ce7 | -9.08114 | -47.00644 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 67e0b80e-162c-39a4-9bad-724e084f3071 | -9.33806 | -55.20665 | 2025-09-05 04:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 122def89-2685-3f7d-9389-47819f15057e | -10.97744 | -45.99027 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaf333b7-afdb-327c-9eba-dc645920c207 | -11.64759 | -52.21632 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae60f4ba-bd33-38b1-aced-e34c3f38539c | -7.79566 | -52.13073 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03a11c8e-2061-3219-845d-2a375ef59c9e | -12.26529 | -50.15147 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 952af74f-5140-3916-a381-23e8cfe0eb9f | -10.97386 | -45.98977 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62ec6fee-72e9-35fa-af9c-31bdd41fd8bb | -11.59389 | -52.18059 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51bb83a3-50ac-3a73-b635-24e172093576 | -11.82857 | -51.42795 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6284f1ab-a145-3a66-939c-33081bdb2384 | -9.97106 | -51.65023 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5880f7b-6125-3ab4-a027-23cb9e8598fb | -9.9623 | -51.63618 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 225ab113-d498-3419-ae11-7cadf35463e5 | -9.51157 | -57.78626 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f49101a-d519-33a2-a9ef-d507327991ac | -10.98057 | -45.94464 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6db2ad3a-13e3-355c-b1fc-004c86aa3a81 | -11.40036 | -43.58093 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17aaac6d-9d98-38e6-b2ed-c47e31ad95d3 | -11.33891 | -50.28559 | 2025-09-05 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b10f9bb0-27a9-32be-ae37-15d6cfc329c0 | -8.08005 | -47.57602 | 2025-09-05 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73caa4ac-c3ae-3dba-8a69-2dfe45dc1d7d | -11.90768 | -46.65343 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90a80b0a-e2b3-3177-91c6-31697c750b09 | -10.76468 | -48.29572 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17c0eb57-89e0-3fba-8a98-ddb0289ad3fc | -12.02433 | -43.78566 | 2025-09-05 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 896bf093-e7c5-3bf4-b9a2-601711c7900d | -8.34916 | -48.29855 | 2025-09-05 04:36:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b0197ae-9fbd-35cc-8912-e9cdd5bda300 | -11.92816 | -46.66016 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0861ccf0-19d8-3373-9012-535c3d016950 | -12.87834 | -48.01199 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0bbedbd2-b395-30d4-800f-117d37a8fa31 | -8.51834 | -51.31707 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cf48457-3c6b-3b3b-ab49-7b49bea18ee9 | -12.86753 | -48.00715 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4878ce42-b5e5-3319-8dd6-389ddf3ed07d | -12.44915 | -48.08232 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74aa8735-0b23-324a-8687-9ea391acf1c2 | -12.41265 | -47.49856 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8dd4f1b-077c-3de5-98fb-31a6364e6a95 | -8.01232 | -45.44654 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c65071f4-4a25-3a36-8ea2-6abf251276e5 | -11.6011 | -52.16003 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70bc89d9-0241-37fa-b294-7f2f78fb79ef | -12.91041 | -48.0284 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d7b9b0d-8dfb-3885-b463-95a546c376cf | -10.47957 | -53.64406 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 289cc2e9-e622-345e-a1f1-7888687b0324 | -12.29126 | -50.01183 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2570d7da-85b0-3a3f-b1b9-8cb31ac51417 | -9.0688 | -50.42785 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fea7b24-ddcf-3a8d-810c-083bfd3490fd | -12.89691 | -48.02625 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 979ee18e-95e8-3b3d-b3c2-9835847fc650 | -11.64796 | -54.53337 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be596e79-f06f-305d-bc34-1005dee872dc | -11.57215 | -44.65725 | 2025-09-05 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bedc84e8-6213-3d0e-8a38-c4a4ee2849ad | -9.80141 | -48.30856 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 545b392c-63e0-3962-87b3-fc898bf2b857 | -8.35051 | -52.51837 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| beedf1b0-54bc-3852-a57e-6f656a126fb9 | -12.50234 | -53.84354 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef75bdf6-036c-3ff6-a2fb-791861a3bcb2 | -10.98459 | -45.9913 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b78e991-d3e8-33e1-a558-f25395e7411e | -7.69786 | -50.29018 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README32.md)

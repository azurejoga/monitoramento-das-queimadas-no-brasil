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
| 02933834-c44b-3513-93d0-f1daa9d0a46c | -9.07073 | -60.41764 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 795123e0-040b-32ef-b711-8643e27ba0a7 | -11.15612 | -50.56731 | 2026-08-31 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34abf01b-5a2c-30ca-9240-03e1f3ffdf5b | -9.0664 | -60.48941 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7727be0-b0c6-36f4-b129-396d47dd9d25 | -11.90634 | -55.89991 | 2026-08-31 05:36:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a6ce639-c1cd-307a-bc62-491469e0825a | -11.49699 | -60.58094 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dbd8204-5682-3173-8691-112a2bcd079e | -10.48466 | -59.60895 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f32d06-55aa-3ef9-9ec8-32d4f5bd536e | -9.89488 | -60.27191 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73b791a4-6783-3734-b731-0f35ea0bc1ae | -9.13824 | -60.53332 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 027b710b-7a1c-3d35-8465-c0879d9a6bf5 | -10.7849 | -50.85843 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7a7e02a-1e01-368b-91e9-f3c4ee7f95e9 | -9.1502 | -61.10303 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f3823d-d811-3de1-bff2-70e27f85a000 | -9.85047 | -64.99141 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fcbb2af2-3f89-3e82-b7a4-74e4d2089f1a | -9.85492 | -64.98765 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dc3faec-7726-3e96-af56-4d66a2612840 | -9.93956 | -60.52464 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c086443c-ec0f-3b55-8755-7408d5d92e11 | -9.89376 | -60.2791 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774a7afb-9d74-384c-97d1-7e27b5f6c1b8 | -9.84384 | -64.98575 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a90b1c7-80d5-3cae-858b-6beb8cfa2bb7 | -8.94097 | -62.37181 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d4f9478-9613-33c4-9514-dc4292127612 | -9.11974 | -60.38908 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59770a0f-bf01-373f-bf15-1b2f1a7930be | -9.06919 | -60.49346 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45c481a4-664d-3e72-ab9f-955447ad1f66 | -10.73795 | -47.96941 | 2026-08-31 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7908597-88fe-380e-a301-81867e7674ed | -10.73942 | -54.04035 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f9eb535b-5848-3344-9271-fec1a13598ec | -9.78922 | -59.43966 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dd27c87-ccb5-3b8a-a0f3-7f85e9006ba0 | -10.74902 | -54.04178 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 877c6c3d-e108-3d21-87f2-007377770e82 | -9.72212 | -64.99854 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a44c3c46-2a9c-3a9d-957d-5d9082b0b9ef | -8.81431 | -70.77978 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e236ff4d-2eae-3af9-8a29-4c487f6288b9 | -10.74472 | -54.04009 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 50a612ca-3a3c-37c0-8a46-43d4c5d94e0e | -9.93113 | -60.49045 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7d8bd3b-f93a-3bc1-ac9f-a9f918d0244f | -11.67878 | -47.60657 | 2026-08-31 05:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5eb9f89-5aa0-354e-b451-a675687147c0 | -11.69369 | -47.60548 | 2026-08-31 05:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df1080c9-b6a2-3d09-ba48-08923a4197a5 | -9.93787 | -60.51342 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e76cbf8e-0310-3a96-880f-f9be50a3e4fb | -8.80179 | -62.49689 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9d4365b-161c-3e0f-9a86-d6d17a42b82e | -9.93618 | -60.5022 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447262bc-52ec-37b3-b493-9a934f196e59 | -8.60397 | -70.20849 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae5ca52f-ecab-3f3e-9698-cf6b429d7ea1 | -10.10408 | -68.40361 | 2026-08-31 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85648818-5511-328b-9663-80ccc419c8ac | -8.67166 | -66.51235 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ab7f420-b7c5-3060-85b8-d7ff146c60ea | -8.678 | -66.52493 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c537285-f524-3f47-bf20-b7b318f17c70 | -8.94885 | -62.36575 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eb92daf-e92e-3e9d-957f-3177b32be493 | -9.93507 | -60.50933 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94f3e10a-8255-32ce-82b8-cbaa0e197075 | -10.57961 | -63.53033 | 2026-08-31 05:36:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 533ca866-a02d-3c5a-aee5-fc8ee933a109 | -11.038 | -57.23 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a08ea90-d3df-3ed7-ba17-707e3bdfc1f4 | -9.8409 | -64.98072 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a03845-3181-3038-a133-9bdbb4049a6c | -8.86768 | -66.78279 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3856550d-ad91-340e-832e-266a028843ec | -11.16467 | -50.5553 | 2026-08-31 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3d3a2a8e-22f6-303d-84bf-cc645b4dfe2e | -10.81021 | -50.65509 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9949fe6c-f2d5-3256-b27e-c8e8e107e87b | -9.71472 | -64.99727 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c76a368-c743-35ce-8f10-51e3f52668fd | -10.73846 | -54.05 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a8e0fbb-946b-31f4-b93c-0140fd7177c4 | -9.21536 | -59.40791 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b40c44df-60c6-3a04-9469-f9b9eb16713e | -9.36828 | -60.31485 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c64b8400-b84e-3833-bc09-688a79389477 | -8.60924 | -70.20954 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b09409de-3dea-32c0-9f70-0565e74b3638 | -9.17814 | -59.63008 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6be1d50-e817-33ff-a6ee-d4098aa8366c | -9.69866 | -65.05967 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62593a55-b986-3547-944a-b731d7527fc5 | -8.00603 | -70.06393 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bc02f1c-f355-39d8-96de-87a2c65e1b5c | -10.5785 | -50.36801 | 2026-08-31 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01f379b1-35e9-35f8-aba2-f7884f7603d0 | -8.83691 | -62.32182 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 485cbc91-ab62-3f2c-891c-7f1493a32292 | -11.95412 | -63.28796 | 2026-08-31 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8c5287b-b177-3e9d-b6dc-d10c27e9f5fe | -9.19193 | -65.51028 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 961a757c-28e9-309c-9d17-95f2885a9eda | -9.06969 | -65.48893 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6802b85f-c38d-3678-ac34-41807de3bf2b | -10.10433 | -68.40542 | 2026-08-31 05:36:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 058e8ee9-0e61-3979-b953-d6c8416f0010 | -10.76707 | -50.85611 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aa66b42-5411-3779-b61e-03352efaba57 | -8.84027 | -62.32237 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6b9c07b-b7b8-39a7-9c4b-03f32e159c7c | -9.36549 | -60.31075 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65773eb-7dbe-3e2f-aa1e-9b72faaf5929 | -10.74833 | -54.04704 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4f6d0258-0f30-38e8-931d-3ba214ae1ae8 | -8.87253 | -66.77972 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c47a243-ef79-3bc8-85c8-09142ac20588 | -8.96712 | -62.38661 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6011e04-e7bd-316e-941a-3fa1d303170b | -8.52101 | -67.18243 | 2026-08-31 05:36:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ada75b53-15d1-397f-a876-eaaf0b13ef01 | -10.48754 | -59.61326 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fef4bc4-d0a4-34ce-9885-02e9f8c7cb50 | -9.85122 | -64.98701 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36a7d5ee-806d-3c91-9f98-406a7241c410 | -10.75054 | -53.99807 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6dd51330-59c7-31a0-b630-c38638dd66f6 | -9.22077 | -59.76076 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3723a46c-b201-3dca-ab7d-1806d3c29cae | -9.2275 | -59.58117 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fdee91b-5dd0-39a9-90a2-1ced55f35b0a | -11.02879 | -57.23855 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e273322-6039-3a5f-9c45-9764af72becf | -11.17664 | -55.09169 | 2026-08-31 05:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05bb6897-9cbb-3db1-a843-2beefa90f669 | -8.79562 | -62.49217 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6d29c82-60f4-3e32-8344-fcd3fd08bc33 | -8.79783 | -62.49994 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0f08b7d-908d-3639-92f5-a0b83bdacb53 | -10.7497 | -54.03653 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6751031-8db3-3a2f-b7f9-944cbc983133 | -9.94011 | -60.52108 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff5aded3-4d3d-30be-8adc-1cbc7dfaedb2 | -11.49643 | -60.58458 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e9a2faf-4350-3c24-a593-d4121b4878fe | -9.05029 | -65.41704 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f653c2e7-6b9f-3550-a58a-24f96dbd6e39 | -9.93621 | -60.5241 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8db551c9-4c50-344c-ae3d-bd2225e266e3 | -8.86903 | -66.77514 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7896f02-0db8-302f-9a91-817de6493b1e | -11.16278 | -50.56347 | 2026-08-31 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9a71063d-b649-3d6b-95d9-f318add293f8 | -9.06096 | -65.42378 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58ce54ac-3352-390b-b453-84908cd17e69 | -8.39548 | -70.08472 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76521466-398c-310b-8bf7-e1ab4a8ee6c4 | -9.93562 | -60.50576 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a32ce68a-786a-3ee9-9b7a-70328c4f91e7 | -9.20985 | -59.55946 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bf681c8-3def-3cd4-aa01-af02a9ebbc38 | -8.68001 | -62.81736 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a00af3ce-66f5-3896-8062-6ef493bbbe5e | -9.89657 | -60.28324 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca002406-cffa-3af5-84a7-50db6045e706 | -11.16359 | -50.56455 | 2026-08-31 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e3fd746-ed80-321b-a483-d76baf6dfdcb | -8.94318 | -62.37954 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e456c33c-792a-35a0-a2b6-731f33c3e98c | -9.46295 | -68.23452 | 2026-08-31 05:36:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df885457-4d6a-357d-a50c-4c7829429145 | -8.94105 | -62.07217 | 2026-08-31 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0d6ba76-93cc-3a1a-909f-6e9f89026e45 | -9.89601 | -60.28683 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc979a2c-b29b-3817-a2c8-5d55e94af26c | -9.71716 | -64.99429 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14fdb050-dfba-3aec-982c-381ee477f563 | -9.84753 | -64.98639 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40b62546-bf3a-3840-98f0-c7d130506738 | -9.2127 | -59.5637 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25619992-9ef9-3540-a4cf-a5c6cd07a23d | -9.84459 | -64.98135 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 177a6172-3b84-37be-bd5f-9daaec8b83a0 | -8.60457 | -70.20523 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ca65b9f-fc69-36d9-8b13-c5bfa9dd414e | -10.47955 | -59.6052 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9acf641c-d00d-3039-9dce-f346938900b1 | -8.94655 | -62.38009 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58b28946-1816-38c6-a52e-04aa415aac45 | -8.86793 | -66.77889 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c7d680ce-fcd7-3ba1-a72d-1006ee2a29c9 | -10.73393 | -54.045 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README65.md)

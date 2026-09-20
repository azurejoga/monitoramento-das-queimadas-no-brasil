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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09dba66a-041a-3a2a-8091-e8ba3a49ef3e | -12.37404 | -45.80336 | 2026-09-20 04:21:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af67b85d-95b5-34fc-b34e-fea20bcedcd6 | -11.23474 | -54.08972 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 405000de-2226-36e1-81cf-ee5b375dd98c | -11.78389 | -47.46885 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e54caa11-5a3c-3dc7-8012-1cebc7096bda | -13.73435 | -48.78386 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 642f228f-9fdc-3908-a852-c61892b7aed5 | -10.87563 | -56.22591 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3f987dc-b91d-330d-af06-ddc2f0859246 | -15.62262 | -47.84263 | 2026-09-20 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70bae278-449b-3dd4-b132-185e0cc001fa | -12.13664 | -47.03782 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b0220ff1-3984-36e4-8708-de05b0e789cc | -14.78513 | -48.53435 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04a30201-e32e-3b56-873d-2321edeb912a | -11.38841 | -51.42651 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd85014c-5e05-3423-ab8c-966df6e457e0 | -11.01841 | -54.12995 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d342d234-f9d7-3dde-bf95-3a2a1694675d | -15.87758 | -49.9058 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4924323d-ac89-3586-8113-b2cdff9548fb | -10.91113 | -53.97256 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3187f200-c757-3d69-9329-7314df200367 | -12.76628 | -52.8579 | 2026-09-20 04:21:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3a6d6ee-bc7e-3ed3-a2a2-7e6d4f6de992 | -11.04045 | -54.17999 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 539ffe90-8ee3-3588-9416-85900029a1d6 | -11.95316 | -50.09949 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef367db3-1c7d-33af-8830-c38490a4d613 | -11.78507 | -49.82292 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de99f392-5caf-36ce-b5df-77ae8ded25be | -12.64206 | -50.92887 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1137cbb3-ab26-3e0b-865a-58e3f56c4fff | -14.92854 | -49.91033 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 773e510f-8896-317f-8c04-a89d8274aa9d | -11.90405 | -47.63079 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95d0a1c8-2ee2-330b-a0d6-d4fc6d59d05a | -11.85354 | -46.86279 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c4c1981-96b8-30b0-b085-8dff5107eb82 | -10.87424 | -53.99914 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05335e04-8bf7-3851-9f9c-12d3d6b76f70 | -15.87184 | -49.91272 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fc7d2c4-0189-32f4-893d-a55640931448 | -11.21738 | -54.08129 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 052ee3e0-7503-3710-8063-6908859bce20 | -11.85596 | -47.66351 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a53f7908-210c-3e20-923c-860fee9bd4cf | -11.09398 | -54.03355 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 995adc5b-cc34-369b-b753-6cfd20ed95c6 | -15.46636 | -48.43596 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79886c84-17ac-344d-b615-28be239784fa | -11.37704 | -51.40171 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b904fcd-cab9-3d41-bdbb-89fe1f6165d9 | -17.98901 | -49.20545 | 2026-09-20 04:21:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1985361f-61e1-35c8-98c0-a2722d45ac27 | -12.69219 | -50.76085 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a91ff948-d6ed-3407-a90e-394d26a6ab9b | -14.67155 | -46.68613 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a908e1bf-d35b-3663-8ce0-9778e16fb36e | -12.28718 | -47.112 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17efc9b3-dd43-3b3c-b067-e87c8e45720a | -16.82829 | -47.6402 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aec974cb-fb47-390f-beaf-dd3413a6cc5f | -14.67518 | -46.68679 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7ccecb20-ec7c-34d7-967a-62c5cd27dd8c | -11.76267 | -47.45781 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8c113da-1be0-3964-a79f-a61df92f06c4 | -12.16206 | -46.95914 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df9fb168-3f52-3677-afd8-f1babf2daa15 | -12.74726 | -46.20428 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa8b08c9-0b87-3d05-a4d1-365eef869de3 | -12.76085 | -46.12381 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7f392f5-ea79-3ad9-9c0c-8222d45ed54f | -12.74361 | -46.18179 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21ab7447-55f5-3ded-a4c9-9505351898a2 | -11.27845 | -54.12008 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9743907e-5e76-3d71-8700-42a4069c281e | -13.03333 | -46.9104 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12de1e37-6268-397e-9c39-40a29ea6f9fa | -10.87923 | -54.09562 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 141ebc52-d5b2-3dcf-b1a1-b71c6d1f96c6 | -11.13533 | -54.01714 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a19179c9-71d5-3c48-88ac-68c5dbdfe783 | -11.78543 | -47.46723 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d57bb842-0480-389e-ad7a-362756ed6527 | -12.13066 | -47.0269 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e32be0c5-4059-3b96-974d-e9c556694784 | -12.12516 | -47.03581 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b15e4942-7d41-36c0-a984-160450c6bbc5 | -18.55297 | -47.23765 | 2026-09-20 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6640010c-1984-38cb-b43f-50c74f117e6c | -13.00785 | -46.92359 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b344bb8a-f52c-3195-b318-9baf771995f9 | -13.01766 | -46.91166 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37ad2b7f-21d7-3c5a-ac09-7958f18fa4c3 | -14.76093 | -48.41157 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85b795ab-2db4-38e6-ad2a-78ca68aeb616 | -12.13365 | -47.03236 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 589209fa-e722-3e78-8178-c74ab90e3a94 | -12.99736 | -46.91721 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07616ee9-7084-3e08-81b1-051a8a645c09 | -11.84895 | -46.8667 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6377f47d-f19d-3d5d-8157-fc08fa6cc424 | -12.73049 | -46.08387 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c08c63f-fb31-3c33-b9ac-e36f58f8e062 | -12.75446 | -46.18379 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d2b88d2-279f-3737-9f6c-44232018a104 | -16.53757 | -49.10489 | 2026-09-20 04:21:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c97bd08-e93f-3967-af01-4ba5d6f438fd | -11.84434 | -46.87074 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce319b9a-f484-3d6a-a55c-75f1325e41db | -11.85734 | -46.86349 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e11bf4b2-703d-3dd6-8682-672604cfaa9d | -11.11419 | -54.02773 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5bb70f11-9f03-3ad9-a73e-86d6aba9f08b | -14.59913 | -48.0999 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c3c9f565-6616-367f-99de-e09632e664a6 | -11.08789 | -54.0323 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0f392efb-dd0a-343f-9e7c-0735664f23b6 | -14.04718 | -52.08566 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69f7312b-415a-3bb9-a0e3-b68664ce4537 | -12.16038 | -47.03725 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4c67f5de-9d97-305b-91fc-203cbaf22f8e | -12.64692 | -50.92985 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d50aaf6-931e-38ab-9628-161acbf38104 | -13.02434 | -46.91767 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 957d852b-a6cc-3e76-9706-ebeffe7317d0 | -11.87584 | -47.67395 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f4b79ec-5671-334c-9d63-6c1731356b76 | -10.91021 | -53.97731 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7470abe5-4c25-3fc9-b564-f15b5338f862 | -11.85196 | -46.87197 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0dee06e2-8a16-38f8-80f7-a2f63b602634 | -12.13448 | -47.02757 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa0bfacd-91a6-3783-be74-9857546b8c1b | -12.9821 | -46.93803 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7947528-2765-3121-b7b9-1bcd35602782 | -11.86099 | -47.44629 | 2026-09-20 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e7b3c39-93fa-3ac0-a7ec-c590bf8e8464 | -12.31652 | -50.72395 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d12cc4da-7d9f-3494-b32f-520e6a658bde | -17.98747 | -49.20343 | 2026-09-20 04:21:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bcb8af67-3c73-38c4-bcd0-0dc72b8b28bb | -14.68243 | -46.68811 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7612aae0-194d-3cbf-a4ac-502583a20da5 | -12.31449 | -50.73469 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0fe26703-fa02-356c-9fdd-7168406ad3e0 | -11.38808 | -51.43317 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb2837be-5b7a-301e-8a74-f6cc7b6e7ff8 | -11.95525 | -50.10286 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e9640c4-3a04-3d77-9597-b54e752cc752 | -12.87771 | -51.01293 | 2026-09-20 04:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05d5a8e9-0fed-3d83-a054-bdc47e49adea | -11.27749 | -54.12477 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11a068e5-7b49-308f-b6ea-8410fb16193a | -11.04329 | -54.16563 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fdba7e0c-e12f-3003-b3a1-34fba9321953 | -12.74941 | -46.19157 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6389e7fe-661d-340f-a230-232a398b48c1 | -15.05936 | -48.58371 | 2026-09-20 04:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53bb64ae-f706-32c2-9125-df0f4dbf88fa | -14.68893 | -46.69375 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 04b6ac94-f30a-3441-baf4-8a1c9b6b1fcb | -14.0511 | -52.0929 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 16a728cd-7b0f-3cc8-8192-4bbd3a308b40 | -14.79316 | -48.53579 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 939e8557-435a-32f2-8f9e-0a7470cdb40e | -11.10715 | -54.03121 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 913167c9-6ad6-34d4-9086-ca44c5e45099 | -11.20503 | -54.0815 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d57f8d78-1777-38ea-a1ad-f8cb407dcdd2 | -11.38508 | -51.38717 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9faf4d47-88d4-3895-accb-efe90c0e24ec | -13.72942 | -48.78732 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 850261b0-1928-3ca5-af4d-9705b3e07b7c | -15.16985 | -48.16257 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c707399d-c4d3-312c-bff4-ffa9f570501b | -14.1818 | -47.87135 | 2026-09-20 04:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6c84399-afd9-3abc-8cf2-9508259a5b31 | -13.23006 | -46.93681 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c35ff64-05df-367f-a33e-0d201002aa3d | -12.75303 | -46.19225 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f425487c-75ac-305f-b1b3-bc4cb436732b | -13.7392 | -48.7808 | 2026-09-20 04:21:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88c7199c-f8f0-33d9-be2d-3b8036d4524f | -11.04753 | -54.17657 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91a31b0a-b5d0-3c39-bc07-97de3894a2ba | -10.85798 | -56.18238 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92d80681-1098-3e59-baf2-1d7efd453fd1 | -11.37132 | -51.40383 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6d88832-a5bb-3c87-a962-0c2c23bf3f3e | -13.67271 | -48.57406 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8e86890-ba04-3a0e-a748-5ce6a25b8b8d | -19.68435 | -44.61332 | 2026-09-20 04:21:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7057a990-015e-3ae8-892b-ccd6e9551088 | -10.86319 | -56.1818 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7f36292c-95cc-3fcc-9723-8b575f4b75e8 | -13.03628 | -46.91569 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README47.md)

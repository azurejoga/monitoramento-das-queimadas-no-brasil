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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86bcfdcf-9ab7-3731-8d98-af4fbaaffbca | -5.72472 | -49.11121 | 2025-07-13 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 146614ce-eb61-340d-82a8-d182cd0607c8 | -5.41732 | -47.56884 | 2025-07-13 04:46:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6159b804-0229-373f-b3a0-439d6b005142 | -5.20946 | -44.35257 | 2025-07-13 04:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50ec1509-78b7-3a08-afa5-6a51372d5e50 | -5.73455 | -44.98473 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 64bfc034-efe4-33cb-a107-24dc4be3a567 | -4.93456 | -46.72464 | 2025-07-13 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a98c04-9901-3006-b768-58ccb88a5ae4 | -7.29071 | -45.31091 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c511b905-012b-3146-b8fa-d61d2bc50310 | -3.86841 | -54.23347 | 2025-07-13 04:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27d23176-b8eb-391d-8fd2-fd6530976c26 | -7.29985 | -45.30821 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 534409ea-2152-3b7b-9c92-af6e939afc13 | -3.61785 | -47.54735 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29a1c710-33ee-3a6c-8d54-2ef0f5decc3d | -7.30901 | -45.30547 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae6da6b4-fcb3-3fa5-b0d8-ddf80065ad4b | -7.33843 | -44.00359 | 2025-07-13 04:46:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b304b276-f04b-3280-8b04-fcf0d7d22860 | -5.73826 | -44.98928 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 62b92410-fb10-3213-bb6b-a52459e2614f | -5.74313 | -44.98593 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 5452afe7-c24d-390e-9b53-63c9356b58a6 | -3.61071 | -47.54631 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7753e80-a547-3b1d-b632-5fc5f0f0acc0 | -4.2899 | -48.05304 | 2025-07-13 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b55a95-a8fd-3dc1-8524-6e19386fcc58 | -5.74429 | -44.97804 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1769e886-f15e-3fac-b891-3bf6200e7237 | -6.10893 | -45.87643 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d89d5d1-404c-3fbd-9f22-624b14ef8699 | -6.31491 | -43.66301 | 2025-07-13 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29deb034-8aa0-3485-a5ba-2c2eb40079a2 | -6.71562 | -44.33023 | 2025-07-13 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c103bb0-1707-388a-9478-c788abdd595c | -5.74742 | -44.98652 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0dbdc7c7-91fe-3ec5-b707-1f062de6b7af | -3.97638 | -48.4174 | 2025-07-13 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e569689-45f3-3096-9998-472a98675557 | -4.53562 | -48.02514 | 2025-07-13 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40282e61-cf1d-3a0f-97cc-367c05f3efdd | -3.82209 | -49.29058 | 2025-07-13 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09a30160-9c83-3bcf-944d-2db89b07cc87 | -5.20882 | -44.35694 | 2025-07-13 04:46:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac3385a8-1aca-38cd-b388-2ded8320da61 | -6.63759 | -39.32901 | 2025-07-13 04:46:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e19d7cc3-f379-36fa-8897-1f6a835f71db | -3.58759 | -47.53031 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c81d733-43f6-321a-bce3-559a834a7bbd | -4.29282 | -48.05743 | 2025-07-13 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34f79245-629a-3fed-bd84-9f7390c60afe | -6.62343 | -43.01725 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e423baef-89a9-3ac9-8573-77796c21a16f | -3.39547 | -46.90869 | 2025-07-13 04:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dcd30b5-8d44-315d-9bf2-f328e0d8886c | -6.94806 | -42.73564 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e5681b00-d02c-31d9-9738-501797c2c84d | -5.73884 | -44.98535 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9779b760-c396-3311-9710-a2b9c846ffd8 | -2.92563 | -48.2407 | 2025-07-13 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b89bdcb-8cb9-35ef-a34e-9d705811fc73 | -3.29665 | -49.19152 | 2025-07-13 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c0749e-e503-3045-b33a-8e808ca347a3 | -5.74371 | -44.98199 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c150518-4ff9-3e27-9273-41b6be52d63b | -7.18491 | -43.0044 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2647fca-bb56-32dd-85f2-87eaf9b9cb05 | -7.30043 | -45.3042 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43b113b4-f236-3684-ab91-2af41240d46b | -6.14376 | -44.09274 | 2025-07-13 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 837203dd-4221-36b8-9e70-c2b18690fd47 | -6.8745 | -42.7795 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11bf0e28-580c-30fe-8549-3517b1ea66c1 | -6.44443 | -45.39757 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 019d0230-46b5-3ec7-88a1-8e6f5bd32190 | -6.6346 | -43.19046 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d776aa03-cc5a-365c-a65e-5d6f254ddd90 | -7.2484 | -46.98392 | 2025-07-13 04:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cab09a0-e246-3ee9-bd63-4482c8fce6ff | -5.27217 | -44.95024 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a205b53d-044f-3471-84aa-a8f3a2259aa8 | -3.97696 | -48.41366 | 2025-07-13 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d9ab4e4-59aa-301f-abdb-261aef3d8854 | -4.45423 | -49.00154 | 2025-07-13 04:46:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9e1643d-3e05-3f12-a130-749ce048431d | -6.1483 | -44.09378 | 2025-07-13 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43acc545-2b9c-397b-bfd1-e8b968fde060 | -4.27613 | -48.18954 | 2025-07-13 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec842c2a-6fdb-30b7-8325-75ce293c26f7 | -4.28021 | -48.18623 | 2025-07-13 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6280ce1f-87be-3f87-9a49-136e9853fedf | -7.78245 | -44.02206 | 2025-07-13 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf1e6492-188d-344f-bfef-d73c8784a507 | -6.74682 | -44.70149 | 2025-07-13 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a19f2520-c11e-33c6-8241-328fd27871ee | -7.29565 | -44.02543 | 2025-07-13 04:46:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ad18866-4039-323f-ab86-a9526351df93 | -7.05135 | -44.33271 | 2025-07-13 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fd50cf1-d26e-378f-8023-a5cfccc6fdbf | -6.31509 | -43.66432 | 2025-07-13 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 001f1eb9-6559-3522-9e30-f231cdcba13e | -6.95871 | -42.73392 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4e4183f4-b424-3000-b1a9-3ce02b3971e7 | -6.82711 | -42.87426 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a59d4d70-10b1-3ab9-bb13-079eace91bc1 | -6.12011 | -45.85713 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 830af27a-f513-35d3-951b-46fc7da062f8 | -6.83296 | -42.8693 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06311bde-8010-34b2-ba99-39d15c5a6536 | -2.92218 | -48.24016 | 2025-07-13 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 082fa84d-5e7b-3826-87d8-9d7d33d0f684 | -6.10946 | -45.87295 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 564c2398-93bc-3acc-bb67-25f45196bbab | -3.40392 | -43.37119 | 2025-07-13 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7b59d41-f95c-3efe-8638-738c391505a4 | -5.27489 | -44.94923 | 2025-07-13 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a62995a-e07b-31f8-a814-081e5a6a8a72 | -6.65043 | -43.11353 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af611644-b1d5-3cbc-9eb4-39f94c95314f | -7.05068 | -44.33734 | 2025-07-13 04:46:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41678edb-d793-399e-bd5e-b8049bc30172 | -4.28931 | -48.05692 | 2025-07-13 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6571e9f-7473-3987-b08c-04fcbbf0f8ad | -3.61847 | -47.5433 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8433f98f-5cac-39fe-b8ec-245f217f244d | -7.08971 | -44.06674 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a20a5d-b149-3955-9beb-95134d6ae6d1 | -7.98653 | -43.39067 | 2025-07-13 04:46:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 29f987d2-8e96-3501-ad7f-e8287309ef10 | -6.87489 | -42.77664 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6a4c2d3-2807-374f-bded-043afee60189 | -6.65538 | -43.11423 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebbfbc3f-ee24-3f5f-a919-e8ba9b73f319 | -6.14344 | -44.09574 | 2025-07-13 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 854eff73-acf2-3556-befb-acdcd7f2d9fc | -7.29672 | -45.29949 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e38e4a1d-9504-3f10-bd18-0b7f0fd28b91 | -7.17912 | -43.00928 | 2025-07-13 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a354c65a-2505-3033-8893-da99bd7e658f | -6.78717 | -43.96559 | 2025-07-13 04:46:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1557731d-ede5-3a11-9c3e-9e313bb10e22 | -5.41784 | -47.56788 | 2025-07-13 04:46:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf491984-1ef1-3f32-9a6f-f256744d5e19 | -7.29496 | -44.03028 | 2025-07-13 04:46:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20c05c47-418b-309e-8c6a-f7c442fe12e8 | -6.62318 | -43.01805 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7beab8dc-fc9c-3a9b-9f3b-1718784f120d | -6.48564 | -45.26426 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c67e217-a1f0-3b08-8643-98b0afdb2356 | -7.98729 | -43.38507 | 2025-07-13 04:46:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9e6bd7a1-e81a-3e04-a40a-3d428d603d38 | -6.13301 | -42.95839 | 2025-07-13 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 76d770fb-cbd7-3a16-8b9e-7a832f8710a1 | -7.99225 | -43.38577 | 2025-07-13 04:46:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b58746b3-b36e-37a5-bfe5-e2e5d96098d9 | -6.12803 | -42.95774 | 2025-07-13 04:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f7aa00e9-642d-38ec-a124-a241136d47bf | -7.48888 | -43.93549 | 2025-07-13 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09b442d3-8d64-3213-aa78-94918c85fd0f | -6.42841 | -44.64349 | 2025-07-13 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12925990-2713-36db-9169-d5f8e73b649e | -6.87177 | -42.77866 | 2025-07-13 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e6c88331-2b84-374a-a652-870f715fd37e | -7.78291 | -44.02369 | 2025-07-13 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 603c2209-087a-3a24-94f4-0a4b60f13ec4 | -5.72528 | -49.10752 | 2025-07-13 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f36cc6aa-27a6-3b18-b36a-788952a7f450 | -4.28871 | -48.06081 | 2025-07-13 04:46:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79f790e2-3d04-35e2-a7a2-affafa3b819b | -7.28528 | -45.31828 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b7c2eaf-7747-3197-a7bf-f6e6c3ed6a23 | -6.64963 | -43.11922 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc2e7f5d-09a3-3c43-af1c-7dbe41b274e9 | -6.48224 | -43.48077 | 2025-07-13 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be424c74-61a4-37ff-9096-13198870155a | -5.72506 | -49.11185 | 2025-07-13 04:46:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3fd9185-a1e5-32fc-b113-9eb0a605f857 | -7.31471 | -45.32674 | 2025-07-13 04:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02e92798-db56-3e9d-9057-7a536697aaf0 | -5.62425 | -44.26578 | 2025-07-13 04:46:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f86ab661-1953-3ad0-b849-546b9b96a85e | -4.78047 | -45.34928 | 2025-07-13 04:46:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 375ef131-9017-3004-be69-fbc3d61be262 | -3.62205 | -47.54381 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8f181a1-78d6-343e-b59a-2cdbe7688eed | -3.97982 | -48.41793 | 2025-07-13 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3423bd5-5ffa-3f4a-8c28-f8a343a9c9e2 | -6.16149 | -45.91432 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8c0fa62-2e16-35e1-a079-3c6e57c9edee | -3.66488 | -48.31316 | 2025-07-13 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c61513da-4663-34fa-a489-5c45a8a657b5 | -6.10893 | -45.87695 | 2025-07-13 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08f03d0d-31e3-3173-9970-1dc3452abacc | -6.62261 | -43.02293 | 2025-07-13 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1e2a524-84eb-334c-bf0a-ac837ef0a749 | -3.75248 | -47.10703 | 2025-07-13 04:46:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README11.md)

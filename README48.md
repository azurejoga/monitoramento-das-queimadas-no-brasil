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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f9c5baa-ddbf-3d78-b6dd-ec04d1450c5f | -12.66646 | -48.01087 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49bb670a-e433-3d75-a1f3-93903e5ae425 | -11.97035 | -46.77918 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8533bfdb-b882-338f-b554-b73aa06af928 | -12.82102 | -47.22534 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6ad114a-28d7-3871-94d1-06ca7b3a0587 | -10.76736 | -44.71818 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e7518ab-1459-398d-b906-3e1c6458da41 | -12.69428 | -47.98633 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e10893c9-5706-30d9-91d2-936ea61b69f3 | -8.42599 | -47.21193 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d33d9d66-7b9a-3593-a479-9b060c6b9f33 | -12.68926 | -47.99643 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44d94ffa-161f-360b-8bee-c13b0ae90360 | -12.29577 | -46.40707 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77c0bcc1-2062-3c7a-843e-624e2082679e | -12.67368 | -48.00842 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f9def1e-cbff-3f91-8ff9-065115b65e9e | -13.79905 | -43.55429 | 2025-09-16 04:29:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2df657f4-b76f-37a3-abff-0dd121ce6616 | -7.44897 | -46.16223 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9ca55437-16c2-3023-b385-418bb36c1334 | -8.97632 | -45.04617 | 2025-09-16 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 663960e4-5d22-3eb8-890f-d59402b9e970 | -12.80355 | -48.593 | 2025-09-16 04:29:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f84b7d4-df14-3c40-99ac-258685725d89 | -10.78308 | -49.14172 | 2025-09-16 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c36b9e9-f3c2-3593-bfa8-034efcd19bc6 | -7.98058 | -45.64077 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80a6c01a-c3cd-368b-aca7-9f2ecbb1e00c | -10.72426 | -44.7646 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb1fcf1c-3d83-3be6-a413-00579964bd6f | -8.42932 | -47.21246 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa0ba6e7-f699-3f14-92af-23d67ece9547 | -11.14449 | -48.09361 | 2025-09-16 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02c5f31d-f1e5-3f4c-bfdb-ad89587fef17 | -11.48804 | -43.60569 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71be85ab-8bca-3896-b099-d5de11ad9b46 | -9.73317 | -46.04115 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c8fc844-523d-3401-bcb0-03992cf76d3a | -8.12527 | -50.1705 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c08fe06e-cfa0-38af-b5b1-209bb7f89e4c | -12.42135 | -47.80398 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3766cbba-b53d-30af-b602-e487f1c2fcbd | -13.21361 | -47.30671 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49734d1a-c6f7-3632-bb3b-a8882f8d7b24 | -9.4655 | -48.58388 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de84ac6a-05b9-3c64-be07-9c01d017aa07 | -8.42171 | -44.97826 | 2025-09-16 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8bd3aab-c799-357c-9cf4-5be864bab44b | -11.42539 | -46.93683 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dc14dcf-06c5-34a0-92ca-10beb1d912d2 | -10.47723 | -45.1669 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c42e810c-616b-331e-812b-26582d1879ef | -8.66443 | -46.36509 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 692c3ce3-b057-3272-beea-8334e7536902 | -7.40803 | -49.9849 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd6e2ae4-69fc-3243-9ec1-53aa120cdbc9 | -9.09443 | -44.83796 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68ff6efb-c3b5-3864-83a9-38becdc5be1b | -9.07228 | -50.31134 | 2025-09-16 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e07c187-beaa-32a9-856b-2b6485f8d3b6 | -8.63616 | -45.68796 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 635d6f6d-57cf-38b7-a8cc-78b76fbaebde | -13.21138 | -47.29908 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57801254-97ce-3ccb-be43-b378bc896056 | -12.92039 | -47.96835 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3b31c47-7920-34b6-9bd0-3eda46e60131 | -11.24298 | -49.94772 | 2025-09-16 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49cf05c1-9c5a-36fe-8ae6-bf0c65398ec9 | -8.95406 | -45.87225 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6080672-e9a6-347c-b4c4-588a7dce96f5 | -11.4354 | -46.9384 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0abc8428-ee55-3f1c-b1ed-a8b4cdb90cf7 | -12.80268 | -47.25518 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cb94a60-1a58-3c6f-99ef-14ca7a69f0e2 | -8.92826 | -45.5193 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fba401f-459e-304e-b9f6-504734809a37 | -9.09995 | -46.92867 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71507267-6408-3a20-9509-ca2a543a4548 | -9.09908 | -44.85401 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8a693908-8217-3f5e-9d52-e4efdaf5af43 | -11.11163 | -45.32707 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed6c1530-71b9-34ca-b586-a5dd87fce6ae | -9.0518 | -44.8511 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c31d2d3d-d33c-39e3-a81c-8c172cfc8b5f | -7.41099 | -49.98982 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53453f18-aad3-3008-9eea-62a5305f97e7 | -11.11048 | -45.33469 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97747ba8-62cf-3ba3-9538-684c80a4dd7b | -10.06943 | -48.17463 | 2025-09-16 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32c5e9de-23cc-3dc2-abd7-9aa9411f9d5b | -7.74073 | -45.3042 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95505da9-8362-35a1-b235-352b040d03d6 | -9.05577 | -47.01835 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f730642d-b467-319a-8abc-0c8ca5841810 | -11.69872 | -46.87147 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40859faa-5c77-33e2-970c-6ba173692aee | -12.8357 | -47.20907 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd3fcbe3-9cb4-30cb-8792-498372143624 | -8.11661 | -48.26593 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8be6347f-be49-3bf2-9fb7-532a52ec8d83 | -12.05504 | -46.56516 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37272f2d-8315-33ee-95c4-639684aad5ff | -12.11469 | -44.82864 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c227e79-0062-34f6-87e2-a07782e36351 | -7.98282 | -45.6484 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c58698ea-873a-369a-adfa-a5e3b510fb14 | -11.65607 | -46.60203 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94023a08-764f-3f2c-a831-ea53acbe6fe1 | -12.69085 | -47.72778 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ba2baf8-6c7e-3d09-a149-1fe5bb666a01 | -8.95296 | -45.87937 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8c304b7-7d33-3ba9-92f8-3e2937c0d4ea | -12.59907 | -47.98909 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bb23fbb-e95f-3275-b447-3fd68fe1be8c | -12.76191 | -47.96074 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24ec274c-97a9-3b6b-aae2-5b551147feb0 | -10.7202 | -44.74395 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e55522b8-9ed4-3c74-b005-e868d56e7aed | -8.62108 | -45.7184 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 417513c5-e82a-3b54-8b10-6c51c05af10a | -9.76166 | -41.88009 | 2025-09-16 04:29:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| caf4950e-0689-36ac-a3e1-e6279905813d | -11.35116 | -47.34424 | 2025-09-16 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d063cb24-9864-32f3-8a5b-09885bcd218e | -12.10758 | -44.82762 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fde8e282-fa13-3f30-b9b7-6d8ec139c282 | -10.63725 | -46.46323 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 959f3cc5-e855-364f-be11-fd1d754a03dd | -8.08759 | -46.83155 | 2025-09-16 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 408581f5-825e-3f24-8d4a-0c91b6569da2 | -9.08927 | -44.84884 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ad55a64-5a23-305b-a5a2-0b3a3aaca126 | -7.66709 | -45.14911 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ab34479-d6b5-3931-a6b6-274fc51f99d2 | -12.06288 | -46.55901 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 03d5285e-d3b9-363a-98d8-33f48b29fc3f | -11.76135 | -46.66619 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9edc6ff-d4f4-3066-957c-cdf9bee9a07f | -8.43543 | -47.21704 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89039f22-9f29-3fa4-8ae3-cd78229e1a9f | -11.44139 | -47.30817 | 2025-09-16 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e91a53c-33b2-3a88-bcd2-4e706d30d002 | -12.6887 | -47.99998 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9b5dd4b-d51d-3fb3-912e-4369531d65c4 | -11.44077 | -43.53323 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 696b1bd0-b044-3d76-b197-76d1cdc0c4ef | -7.95324 | -45.66182 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d395152-f55d-3d6a-a875-fca62ac2e1d8 | -10.71902 | -44.75175 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd334f70-492d-39bb-9035-d9d9d57f9875 | -8.12662 | -48.26689 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac0b86f7-54da-3581-a398-7abb9b907b82 | -12.79601 | -47.18837 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aae1f0c0-dd14-3dcb-bfe9-50a903f705ca | -11.12658 | -45.34497 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7327c3f3-7d01-3c69-a70e-450096796838 | -7.86629 | -48.15022 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 695b886a-e480-38eb-8066-335be4374ad0 | -8.13536 | -49.37924 | 2025-09-16 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c40dcb7d-b428-392a-984e-48df347f3754 | -8.67827 | -49.93933 | 2025-09-16 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c0646a7-eef8-3187-8a99-1ce9a6d62399 | -12.7719 | -47.96238 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d892b39b-bee1-3f20-bbc6-5a0868291386 | -8.61461 | -46.38607 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2125e73c-63e6-3595-ae52-07983aa8b278 | -8.8934 | -46.15303 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95a58287-752c-339c-aa4a-3032acf5d344 | -9.13767 | -46.94904 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7f526778-bc7c-3b1e-833a-7b6e7ed8e6e0 | -9.09552 | -46.93512 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 608ae92f-1369-3be0-9c0e-d89722ad6bc9 | -12.68528 | -47.7414 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc27bf9b-6a89-34bb-be39-65af90ce426f | -12.11649 | -44.81668 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ccd3bb6-f1dc-3fac-82ee-7a73a63bb964 | -8.98905 | -45.75728 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 746a1fcc-7eea-3020-92d9-fe8d48faa514 | -7.71285 | -55.45353 | 2025-09-16 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1327b0f1-11ea-344a-b9ef-44ab9078d2e3 | -8.6689 | -46.38014 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef6229cd-3899-352e-9fb8-29aaba2fe0f9 | -9.0887 | -44.85262 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5e13e55-f002-3bad-8d91-4fca7a385e01 | -12.06343 | -46.55542 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7030de8d-dfb0-3de9-bf97-624a6eb1000b | -9.48621 | -55.96848 | 2025-09-16 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54596a6d-45c0-3bde-94b6-49b8c78cbb83 | -7.40657 | -49.99357 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5895bc05-a582-318e-ad38-cbe9bade955c | -9.05871 | -44.85216 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 286ce58b-20c3-375b-8d04-20e3512b9a74 | -11.08144 | -49.74671 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eccd772-1fca-3eda-b1fb-ec60e2578c5e | -7.62794 | -46.55141 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ad89a4e-855b-36e3-9cf2-c88d391e743e | -7.4073 | -49.98923 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README49.md)

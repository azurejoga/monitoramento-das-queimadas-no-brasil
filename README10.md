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
| 5666a664-caaa-365a-8f82-2e136ca4c443 | 4.27191 | -59.90316 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c8b2a1-2e98-30ca-bd8c-925403daf85c | 2.41707 | -60.10973 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 675bbb5f-28be-3cac-9f8d-84b4d1d0c3ae | 0.09066 | -60.62377 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 937fe06f-50ef-35ce-85d6-95b851b0a83c | 0.49679 | -60.49272 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa6a812f-ba5b-37d2-8646-4f79e9b1235c | 0.31252 | -60.43962 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0685026-f3b6-3e40-9bae-7deac8150c55 | 1.36239 | -60.37819 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6800f051-104b-31c9-ab41-d648c43f88ad | 0.96313 | -60.52961 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f936e6e-2b6b-39b5-abd7-50c2b2d448f0 | 0.93121 | -60.53902 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1fc7229-6e74-3ce8-8f92-2511243d6fae | 1.33908 | -60.06494 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55106c30-fd48-3f92-a69f-c86556dfd063 | 0.94156 | -60.18427 | 2026-03-03 05:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 329f622a-e87f-3f57-bdac-8b1f3dd08536 | 3.15952 | -60.69825 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4595b9e-acaf-334d-8b49-87072b93f67f | 4.24075 | -59.91572 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f783189-e502-35f4-87fd-7373e7151193 | 3.18632 | -60.68596 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04e9c8ea-d693-3232-b81b-f1ce1a73d8c1 | 0.77158 | -60.47614 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6520e8bc-2c41-337a-83ae-2a28ba78e1ac | 0.94526 | -60.18371 | 2026-03-03 05:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 203523e9-d994-39bf-bc60-432fe2a1a0f3 | 0.87121 | -60.46925 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00800bbd-9338-3c24-b107-119968520738 | 2.86624 | -60.81351 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b861e024-d452-3d7a-af63-8d7d100ae739 | 3.18055 | -60.69485 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73b31a18-f439-3a69-995b-c317e1f55b4b | 1.55371 | -60.28576 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e96ef838-383b-35e4-94ca-4f54995c43b2 | 2.90706 | -60.61481 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f7fb39-a2ca-32bc-9804-10e25eb7ba30 | 1.48066 | -59.92453 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a00352ec-154e-312a-a967-da51f26b195e | 4.27322 | -59.91139 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95b0bbf4-9850-399e-9e53-7701360cc99d | 2.79861 | -60.72802 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32d11fd8-711f-3c65-9862-cfb0505a23aa | 0.23467 | -60.51526 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b87b7b6-83f9-35f6-855c-30829b5292a6 | 0.49449 | -60.5018 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2a475d5-33fa-3c18-804b-330d0c236090 | -1.50762 | -54.52285 | 2026-03-03 05:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f97d0f90-7dca-3ba4-859a-6b2fb0b29c9d | 1.51484 | -59.92369 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2948c5a5-35d0-3504-af1f-71d8819c7686 | 0.80121 | -59.87119 | 2026-03-03 05:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b2dad59-4728-33d9-b761-0b7ce9aa7712 | 0.70071 | -59.96838 | 2026-03-03 05:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97463d8d-2869-3bca-b06a-c2bca3b06544 | 2.89134 | -60.62946 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 798c72e3-b17f-3c15-8b41-1f76e3f714de | 0.92528 | -60.43189 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a522d19c-ace6-395d-bcd7-80c3a57ed9df | 1.35732 | -60.06791 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f52f2be8-3ce7-3595-9465-e0c40f20c423 | 2.8204 | -60.84069 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a7fba0e-de02-3f28-8681-66c3b0496b42 | 0.30952 | -60.44448 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27f816e3-699d-3906-a400-34925cff1c85 | 0.17503 | -59.42791 | 2026-03-03 05:42:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 703efa75-7da2-3e8c-8403-6cc7b9a61a91 | 1.51042 | -59.91986 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37e9c66c-3e5e-3d7d-82ed-b87de1d4787b | 3.16776 | -60.70481 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed5ba85b-8104-3ea3-85c3-485dcb0aa14f | 2.32192 | -59.86919 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af1f2ba1-ad06-3877-bcfd-5415904eb963 | 1.35518 | -60.05481 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dfc85d5-52e4-393a-b2ac-0633b81dc125 | 3.17995 | -60.6911 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 622d0400-4b5a-3833-b17c-279ec482fd19 | 0.45475 | -60.39404 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17719242-dad3-38e1-8de0-c27bab79ac1a | 1.64791 | -60.24165 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8366e3a-71a9-3d07-83d4-307e592a817e | 2.6771 | -60.42332 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0bf8b3b-0be7-3285-9965-633a3571a734 | 3.02769 | -60.66574 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ffb7ef1-4563-386b-a3ce-4819c4e717de | 0.87418 | -60.46445 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05dbd9d0-c9af-3402-bbb9-601bbf272deb | 3.03057 | -60.66125 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e8d18ca-922c-368d-862c-42e40111f211 | 3.11987 | -60.47321 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4383015-444d-31ad-8197-21b371aa69fa | 1.51415 | -59.91935 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d44e7b5b-ae9e-3344-9c3e-9fddf4e5214d | 1.73036 | -60.54936 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a0408e6-9223-3544-a4f3-dfd2f86dcd48 | 1.65088 | -60.23682 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23dd6ef8-caec-32e4-8708-e8b06ef3b31d | 1.94998 | -60.51781 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feed62b3-0a8c-35ab-9f27-60873063f4ec | 0.09133 | -60.628 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86a6eba4-9d05-35aa-bfaa-d2fef00be90f | 1.11509 | -59.20173 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9df5866-b637-398d-9229-6c61efd77f6c | 0.05927 | -60.97214 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7906fc0e-a68f-3eb6-aed4-c29d0dfa124e | 3.15891 | -60.69441 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f1c64a4-be9c-3501-83ad-2916a39c4d0a | 1.48736 | -59.9188 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f127827-3721-392b-a695-3a7c27c339c6 | 0.66577 | -60.35519 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ded297d6-f007-3073-86d7-4dda444c4a6b | 1.48863 | -59.95041 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce36829b-d59b-3b93-a3eb-50111fe09bd5 | 0.49652 | -60.51453 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 998f4a22-2014-3949-aa69-99dfa2b92f8a | 4.26269 | -59.89158 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91822ad2-3247-3ea9-b155-cb5838181a1c | 1.11814 | -59.19739 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d40a78cd-0c2e-3a29-bbbb-1ae10ecc0d60 | 1.48665 | -59.91434 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6171a2d-8b42-380c-9460-219029569620 | 1.4732 | -59.92559 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff7e3a2a-17bb-37bc-b93c-e7ed1b2ce495 | 3.12406 | -60.47665 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5aaad6f9-0e1b-3869-ab92-eafde1c0ce51 | 1.07516 | -59.25451 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fab428f0-6e59-33c2-8777-43e5ff95f781 | 3.23813 | -60.1314 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87d274b5-0c82-3ae1-99e5-a60633709849 | 0.08701 | -60.62433 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c1a6645-3428-3bf6-90a8-35be156d867b | 0.56688 | -59.91032 | 2026-03-03 05:42:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa940f07-75ac-3d1c-81fd-726707c3f928 | 1.96008 | -60.51205 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f233afb1-5f1f-3232-b87c-2bd40ce1f4b4 | 1.3603 | -60.06295 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7eaac9c2-cb31-3e81-a73c-3d736d2389c9 | 1.35687 | -60.05759 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9834adc-4276-3287-976c-758b46ab8e9f | 1.50528 | -59.9116 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5279680f-d19f-3a6e-a426-7cd523f2b54c | 3.15539 | -60.6949 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bc952fb-075a-312e-b49b-679d1f7918fc | 1.35619 | -60.0532 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a42d757c-77d0-3962-b9ac-51823725c680 | 1.35234 | -60.03734 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68187090-73e3-3d4d-8caa-b80d5b507a2b | 0.45107 | -60.3946 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be013064-10ed-328a-ae6a-b383129e9c4b | 3.43885 | -60.60732 | 2026-03-03 05:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae0d910e-9dd5-3903-8a77-e1edfeda9bf6 | 2.90769 | -60.61876 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d26aa2b3-70be-3ea9-8cd3-a8384d3bd5c9 | 3.12052 | -60.47721 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c5b4db9-bc37-3a73-8603-1081eccc2dcc | 3.23453 | -60.13196 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd41cd70-9ff0-324b-befd-8f17cdb5a67c | 0.0799 | -60.55576 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d53303b4-d211-3587-93f3-73a7003f848e | 1.11819 | -59.19621 | 2026-03-03 05:42:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ba797b-9db3-3b0b-9737-da1cb6f3ea14 | 3.16426 | -60.70537 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 428c44f9-daaa-3743-8739-54dc7aea17f0 | 0.94236 | -60.18271 | 2026-03-03 05:42:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae40a38c-abdf-3e96-9f48-5e1655b8095a | 1.49712 | -59.90826 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ead320f5-e328-3dd5-9634-cc3b0e323288 | 2.68766 | -60.06606 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d94c005-0315-38dd-be60-16bef871626b | 4.28011 | -59.92029 | 2026-03-03 05:42:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 058d4278-0b79-3e67-871a-88fe24f1cc8c | 3.18344 | -60.69046 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e201b65-bf97-3e89-9b88-dfa55b4f0e91 | 0.41303 | -60.57804 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d1a6cf3-087a-328e-ada8-4f512923f01a | 1.86547 | -60.40435 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5a74c71-70aa-377b-89c4-167566d488de | 1.78268 | -60.54242 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40feeed1-2923-35d6-9231-ae501cc9b296 | 1.95356 | -60.51723 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84824483-580d-3721-a934-e735d178102d | -0.48626 | -64.60277 | 2026-03-03 05:42:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1a0efd7-f226-3c07-95f5-9a06ddfb9cf7 | 0.31319 | -60.44391 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e875d9c-7eac-36f9-8158-7de50573205a | 2.68471 | -60.07087 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8861c248-1c3b-3baf-a55e-ab32ca63ff0e | 1.51321 | -59.93742 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c62d913-d113-309d-8f92-1b3867889287 | 1.4941 | -59.91322 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fdb3cac-5ab3-3fa5-994f-9c4901d4a108 | 2.68108 | -60.07145 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b72f8d91-1b6f-33f9-ade8-2dcacc3735cf | 0.23413 | -60.51336 | 2026-03-03 05:42:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be36a261-b20c-3f53-b8a7-61772f229a07 | 1.47392 | -59.93005 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)

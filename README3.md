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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 611b60dc-030b-3352-a1ca-2ca770282a59 | -20.18642 | -46.48304 | 2026-03-02 04:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d2afa00-8539-39b6-8e1b-423456603ab1 | -21.3788 | -48.63648 | 2026-03-02 04:25:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a819d37e-7031-382e-8c8b-9f1a95cb9ed4 | -17.53 | -53.69837 | 2026-03-02 04:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab2cfb88-2939-3011-be34-2d8d560588ba | -24.33388 | -49.72976 | 2026-03-02 04:25:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f8a7a9e-c692-3b6f-9896-3f66ce5be305 | -18.79935 | -57.61925 | 2026-03-02 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4e5058f4-9b8a-396e-b2b2-946d7e8c732c | -18.79326 | -57.62154 | 2026-03-02 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b9001340-de59-364f-b4e4-1d3f11f9ac13 | -19.13828 | -52.62234 | 2026-03-02 04:25:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454ad2c9-eca7-3e32-978a-2addffa11e8a | -17.52741 | -53.69952 | 2026-03-02 04:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 443199ef-78bc-3ec3-b0c4-8e4ba6286501 | -23.61348 | -46.53822 | 2026-03-02 04:25:00 | NOAA-20 | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0925cd6f-e324-3f56-8e42-358b6684293b | -21.91401 | -49.44618 | 2026-03-02 04:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4ec626e-5308-3f7d-9aa6-ee45eac4b2d6 | -18.7925 | -57.62513 | 2026-03-02 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| cb72a96b-c6d4-33ac-ab06-14e035465586 | -18.80188 | -57.61862 | 2026-03-02 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c80cb3a2-48d2-3e1a-8509-185db2f836ca | -18.7986 | -57.62284 | 2026-03-02 04:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b43e1d48-1d71-3ad9-9bf5-14283a588650 | -24.33056 | -49.72913 | 2026-03-02 04:25:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20524acc-0a77-3e9d-97a5-5bbf8f1a145b | -21.91068 | -49.44556 | 2026-03-02 04:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1bef4a6e-156e-3898-b263-9872f816bfb4 | -31.7635 | -52.2555 | 2026-03-02 04:27:00 | NOAA-20 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 3b49a089-583d-35a5-a8d7-50895d0c01a7 | -30.10486 | -52.6781 | 2026-03-02 04:27:00 | NOAA-20 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| d889cabc-ae55-362f-b8ff-e101a92c73bf | 1.5047 | -59.9116 | 2026-03-02 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 1d2f1a69-9385-3af5-aed5-831a1702b1f9 | 1.4864 | -59.9117 | 2026-03-02 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| fe84e82f-49c5-3759-803f-285733f8771a | 1.5046 | -59.9306 | 2026-03-02 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b80ae5e4-0b12-3a98-97cf-13829b29143c | 1.5046 | -59.9306 | 2026-03-02 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 759b2cd5-8589-3ecd-85ad-79487b90dd88 | 1.5047 | -59.9116 | 2026-03-02 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 965d0c6a-0b7d-3723-babd-5c3e74592088 | 2.8536 | -60.8259 | 2026-03-02 04:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 74dd6007-3195-3f3f-bc4d-adeea14c4b04 | 1.5229 | -59.9114 | 2026-03-02 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| e711e50a-7641-381a-88d6-38670c4d3866 | 1.5047 | -59.8925 | 2026-03-02 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c1e8b642-0ef3-3012-a096-ff47419292ab | 1.4864 | -59.9117 | 2026-03-02 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1d065c2b-b738-3d03-b2ec-6b02345441f6 | 1.5047 | -59.9116 | 2026-03-02 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 7fb99ca0-cfca-35a0-b28c-6687f258fe98 | 1.5047 | -59.9116 | 2026-03-02 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.0 |
| ebd87e2d-c04e-38dc-a36f-edbaf15fce56 | 1.5046 | -59.9306 | 2026-03-02 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 29b17e3e-3fe4-3b8e-96cf-7b7f2c8e9f7c | 1.4864 | -59.9117 | 2026-03-02 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2028582d-a978-3604-94b6-04702a2622f6 | 1.4864 | -59.9117 | 2026-03-02 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a6ca603b-a207-341b-9b21-01167315f416 | 1.5047 | -59.9116 | 2026-03-02 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.7 |
| b7e7b190-8679-3d3a-943f-979eb6c57f24 | 1.5046 | -59.9306 | 2026-03-02 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 277de5f6-3675-39c8-bf15-c940fff33876 | 1.40612 | -60.74422 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b385a0d-7ffb-3f90-aea2-85fc1db2e3cc | 1.47212 | -59.92577 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75b2e7d4-e0cc-3d42-9aac-c500e04e9668 | 1.93875 | -60.37285 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78dd57dc-f57c-39fa-9c21-03056cd1d93e | 1.2001 | -59.97078 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40ef0df5-c028-336a-b31b-4038641dfb55 | 3.17422 | -60.69178 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e92ebee-239c-3844-ad5a-04470a6d1e2e | 1.86767 | -60.40563 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a90345f-656b-38d5-8999-93f73eb77b86 | 2.86147 | -60.81927 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b07cf9b-fb43-3453-9ad7-52de4d307bd5 | 0.4948 | -60.49712 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5f3fc310-4f38-3540-91e7-6777f8c3f568 | 0.11279 | -60.62627 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af23ed85-e872-3686-bd02-40af654d40fe | 4.0797 | -60.13868 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81457630-a552-3df0-a05a-761b396be76e | 3.02039 | -60.68992 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07b630ac-07e9-3328-8c93-9d18ca42b221 | 1.09519 | -60.68187 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efbaa9ce-9e5f-3d9f-86a3-d18be67499af | 3.16603 | -59.90752 | 2026-03-02 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d20f9cd8-3259-39e9-af44-eb8db6e65523 | 2.85908 | -60.83109 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85292bcf-0624-3e61-bff5-36208f9c7f78 | 1.09596 | -60.17468 | 2026-03-02 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 67d50edb-47b7-3840-9b7d-c6352510c154 | 0.30851 | -60.49054 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89739093-b32b-34aa-8c82-232bea1c99e8 | 2.86025 | -60.83858 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 756f6db1-b484-3712-a7a9-15057059f6d7 | 1.50198 | -59.91633 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 49a994cf-47b6-3d42-8a9f-c8f5e1aa9a17 | 1.07864 | -59.24936 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f8ff341-11f5-3c84-8a3f-ec2059d5d0d7 | 1.02386 | -60.53798 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5248604-1769-31d0-a9fb-eaf95e5adb6a | 3.18971 | -60.68269 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93a7a274-9967-35f8-919c-29572c29b262 | 0.09477 | -60.63929 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17af1e78-82fc-3a51-9c60-a3efe62cc8c9 | 3.42083 | -60.8373 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 511fdc10-ddb2-30a4-86cc-c976a6928bd4 | 1.06034 | -59.25216 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d51ae29d-5cdc-3935-a735-d82970c96f41 | 0.92218 | -60.52977 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc950124-da5d-3b8c-91f8-02e69b1626b4 | 1.20082 | -59.97539 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 568e9f3a-f56d-395c-8b23-97148ed0667e | 4.2545 | -59.91028 | 2026-03-02 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d8948c80-f527-3058-8310-afea1cc0d01b | 0.0526 | -60.98066 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbb15726-a5b3-322f-b0f4-7520f8b2d4bb | 2.86031 | -60.81183 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 357ba561-d7c0-36cf-beff-d0dc5e54da19 | 0.09318 | -60.62931 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88ef75fc-1af6-3d45-b853-553b18bc7575 | 4.08225 | -59.8832 | 2026-03-02 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de01bc87-9b76-3350-9596-2a9dc01e8904 | 1.51186 | -59.92939 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87d7c40d-2b2f-39e1-bddb-9baba6d43608 | 0.79983 | -59.8687 | 2026-03-02 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dbd09bf-77d7-3fe0-92db-de00098b1f4a | 1.49052 | -59.91814 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 521ef85f-2bef-3f14-9447-3c4edf71814e | 3.02748 | -60.68133 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8336db3-d6f4-3625-9f31-3e7fc27c67e0 | 1.06333 | -59.24733 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94cf28e3-750f-34de-94b1-29768aabd9e6 | 1.77884 | -60.61365 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33658de4-4a75-37b5-a09d-7ab5976a833c | 3.03158 | -60.68073 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c00a80c4-ad39-38af-96a8-e8c8ca070e31 | 1.50272 | -59.92108 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c4f94df7-3c8c-376a-924f-fd72a0ba3aee | 0.7399 | -60.1582 | 2026-03-02 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88d7dae9-9666-3966-a757-3e699b74561a | 4.38394 | -60.61729 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59ca7380-3ae9-30df-adc0-c7d923b8292c | 1.50728 | -59.92515 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d910e8e0-78cf-3e6b-ad65-1af80d4068d7 | 1.51261 | -59.93417 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8240e48f-2b92-3a5f-891a-18e47f1f69f8 | 2.8508 | -60.83231 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| edb7bdec-5d17-3df9-be00-a4bf87ca92aa | 0.48854 | -60.50829 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50c6f05b-5636-32d4-9da4-e6bc3a4ed520 | 3.1712 | -60.6918 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb00945c-5259-31fc-aeed-8e5196161598 | 4.37196 | -60.6228 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| abe881e3-7fd0-30d5-92d6-5fd5e1fb6ec9 | 2.85999 | -60.81982 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1640d2f-2343-38b8-b4fd-c327afff4018 | 3.03512 | -60.67645 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 310afab8-b42f-3fe5-8711-1cfd05a2d125 | 2.86089 | -60.81554 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c51b0f6-c63c-33f0-b346-250c08f7e699 | 2.85313 | -60.84731 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b433c03d-08cc-3dfd-a4ae-aca76b59ca1a | 0.69859 | -59.96696 | 2026-03-02 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45186cee-4f27-30e6-a096-84df20fac1cd | 0.7031 | -59.97099 | 2026-03-02 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8b6d4e1-e69f-3190-a361-443898e8d817 | 0.65578 | -59.61598 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9110ade3-6840-3845-8252-e102dbc51c49 | 1.86305 | -60.40197 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 001fcb7a-54c1-3454-909c-9933494321d9 | 1.08596 | -59.24824 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8076229-f325-358f-9308-e903b5c2c88e | 0.11331 | -60.62897 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea80dc22-07f4-32cf-b192-b3c9dac4757b | 1.86623 | -60.39627 | 2026-03-02 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2a75c77-a620-320d-94b9-2536e906c905 | 1.12237 | -60.52513 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d70f4da3-4b95-35e3-b9aa-eed90bace03c | 0.96144 | -60.23766 | 2026-03-02 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893919aa-7afa-3d3d-bfeb-a478dfe99870 | 3.03923 | -60.67583 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a99105d-c001-3f98-a760-a0d57a4f9c4d | 3.18914 | -60.6789 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48bec37d-807d-3c9d-ab54-ddca11f3dd0a | 3.19741 | -60.67794 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0eded34-db87-318a-91b9-56c58d031893 | 0.18783 | -60.44086 | 2026-03-02 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1083ed0-576e-3447-bf8e-437465239a57 | 1.06467 | -59.25588 | 2026-03-02 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50775647-2ebd-3b66-8e5f-a3cd350a96c3 | 3.18197 | -60.68726 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7378b3bb-8566-30b2-ac22-692e4d57cbb8 | 1.51417 | -59.91916 | 2026-03-02 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README4.md)

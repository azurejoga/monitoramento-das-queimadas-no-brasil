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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 433bdc5e-3264-3375-9800-5245323f4217 | 1.5046 | -59.9306 | 2026-03-02 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 5d180eee-981c-3797-8597-419573141227 | 2.8536 | -60.8259 | 2026-03-02 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 806fb747-eb03-3d72-8c86-63507f9fd208 | 1.4864 | -59.9117 | 2026-03-02 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8f0c15ac-db28-3029-a44c-8b549a324eea | 2.8535 | -60.8448 | 2026-03-02 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 0424fb1c-a9f3-341c-9ab3-2eb38605c170 | 1.5046 | -59.9306 | 2026-03-02 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6b13b559-df96-33be-ad79-93598c675858 | 1.1031 | -60.1808 | 2026-03-02 01:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 444b5a49-72c3-372a-91bb-5eb4199b4267 | 1.5047 | -59.9116 | 2026-03-02 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 09918245-cfa4-36c5-bc68-84077e4e6d5a | 1.4864 | -59.9117 | 2026-03-02 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 155a0aae-b44c-354f-8e92-8ff104f7fba0 | 1.1031 | -60.1808 | 2026-03-02 01:40:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 207985e0-0fb6-3fda-93ef-c0e795d0f841 | 1.5046 | -59.9306 | 2026-03-02 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5102a70f-4a89-3369-a25a-5943562303f4 | 2.8536 | -60.8259 | 2026-03-02 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3fd28307-80f4-30b0-a269-2551614b35fd | 1.0849 | -60.181 | 2026-03-02 01:40:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 067eb9b8-136a-3bb9-a18d-b52b007f8dd3 | 1.5047 | -59.9116 | 2026-03-02 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 16e5e0d0-bca7-3db8-873c-7d17bc5acca6 | 2.8535 | -60.8448 | 2026-03-02 01:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a87d4ec6-46f4-35cf-a06c-889c28efad18 | 1.0849 | -60.181 | 2026-03-02 01:50:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1bcab8d5-82f0-399c-b9eb-6e2db5248ad5 | 1.8689 | -60.4024 | 2026-03-02 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 47f75638-24ab-3a1e-9a0f-b0a78f0a137d | 1.4864 | -59.9117 | 2026-03-02 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 038e6d6f-0b58-39de-a903-8ff1bcdef3d7 | 2.8536 | -60.8259 | 2026-03-02 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5dea6cba-dbeb-303d-b3b1-591278fdd275 | 1.5047 | -59.9116 | 2026-03-02 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 8ea50d8d-be6b-326d-8369-cf32346ce778 | 1.1031 | -60.1808 | 2026-03-02 01:50:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7bc74b7a-c1f7-3a15-bf05-1f46ddf31732 | 2.8535 | -60.8448 | 2026-03-02 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 92.1 |
| dec70615-4bdc-325e-aadc-7414498c0762 | 0.4648 | -60.3925 | 2026-03-02 01:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ccaa9b5f-de19-3b17-b233-464bc514ae64 | 1.5046 | -59.9306 | 2026-03-02 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 776f29ff-74f8-39e5-9209-0b96a5e31951 | 1.4864 | -59.9117 | 2026-03-02 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| efb1c063-d015-3a98-95de-f39e0c205edb | 1.1031 | -60.1808 | 2026-03-02 02:00:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 3b5dea73-2f01-3a07-a0c6-05545f0efabf | 1.5047 | -59.9116 | 2026-03-02 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 114.8 |
| dd1f116a-fe84-3a10-8475-b42722dfb410 | 1.5046 | -59.9306 | 2026-03-02 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c285724d-c2c3-3b1e-a364-fad214d3b771 | 1.1031 | -60.1808 | 2026-03-02 02:10:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| eacb5143-6d01-3150-8e2e-d3ced9978532 | 1.5047 | -59.9116 | 2026-03-02 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 28deeff5-4d87-3d30-9e43-7ea2a906eb63 | 1.5046 | -59.9306 | 2026-03-02 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c02ba786-cd8d-3c8a-8664-c206cf56533a | 1.4864 | -59.9117 | 2026-03-02 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b18676b9-b228-31ab-aa48-aba2e67302d7 | 0.4466 | -60.3925 | 2026-03-02 02:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ffe92c3f-b84b-335f-a417-812e22d7a898 | 1.5047 | -59.9116 | 2026-03-02 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.0 |
| f05a5551-54a8-307d-b32e-e4150a91f16b | 1.1031 | -60.1808 | 2026-03-02 02:20:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8af68334-196e-3e72-90ae-700835c6b1a9 | 1.5046 | -59.9306 | 2026-03-02 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3f5489fc-0ecb-3379-91f0-aaa23f99490b | 1.4864 | -59.9117 | 2026-03-02 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| dd3cd963-4e6d-31a1-96e0-1efc6e41615c | 1.1031 | -60.1808 | 2026-03-02 02:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 3d51a141-1935-3f71-a6ad-aafa197af547 | 1.5046 | -59.9306 | 2026-03-02 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fdfc0594-fa5c-3c4c-badf-a9cd63a2ac5f | 1.5047 | -59.9116 | 2026-03-02 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.5 |
| df40d49b-1848-3226-bf91-eb926ca52017 | 1.4864 | -59.9117 | 2026-03-02 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8ebbe550-daed-32fc-b810-d2e51bd4c05e | 1.5046 | -59.9306 | 2026-03-02 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 906a20b0-4c2f-31b7-bce9-31af947692b4 | 1.4864 | -59.9117 | 2026-03-02 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f396055a-f02a-3ca5-9834-3746838a01fb | 1.5047 | -59.9116 | 2026-03-02 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 7a029a16-7ae0-3853-b76d-4f6f14f070fb | 1.1031 | -60.1808 | 2026-03-02 02:40:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 5c97297e-6859-3663-97e2-1e4e9df69f4c | 1.4864 | -59.9117 | 2026-03-02 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 301a5eb0-c5fc-3045-9641-0c5377aa6cfd | 1.5047 | -59.9116 | 2026-03-02 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 46198c11-4514-3195-a63b-8d9ae8ea31d4 | 1.5046 | -59.9306 | 2026-03-02 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 639fe4ed-6cdc-3530-b090-b4195f307bd1 | 1.1031 | -60.1808 | 2026-03-02 02:50:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b1b2b754-68da-3b5c-8459-68156c791300 | 1.5047 | -59.9116 | 2026-03-02 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.5 |
| d2c73b7e-af17-3a00-8fec-121c21b125da | 1.4864 | -59.9117 | 2026-03-02 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3221d0ab-e83f-350f-b7c4-abd7922553b4 | 1.5046 | -59.9306 | 2026-03-02 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 28e9a1ed-eb7b-34f1-88d8-2caea23b8262 | 1.1031 | -60.1808 | 2026-03-02 03:00:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d5557cdc-9420-370a-8bfd-972f0ccc11a6 | 1.5047 | -59.9116 | 2026-03-02 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.9 |
| db795dc0-dd6e-3f80-ad64-4ffb8d7f3d38 | 1.4864 | -59.9117 | 2026-03-02 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ec8808cc-919b-3519-bad2-64ba8b11a0b6 | 1.5046 | -59.9306 | 2026-03-02 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ac418067-fcdf-3f73-b041-81349ac08813 | 1.4864 | -59.9117 | 2026-03-02 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6ff17f38-005d-3e06-8d6f-d1e37f244436 | 1.5046 | -59.9306 | 2026-03-02 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 9bade7d8-144f-3a79-8cc9-822207f34169 | 1.5047 | -59.9116 | 2026-03-02 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 106.9 |
| e65e9423-493c-30e9-8942-0e843eb4265f | 1.4864 | -59.9117 | 2026-03-02 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a9ae6aed-7a09-340d-bc1f-b917f02649a3 | 1.5046 | -59.9306 | 2026-03-02 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 2acd95d5-48fb-38de-9670-af624686c206 | 1.5047 | -59.9116 | 2026-03-02 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 9efd08bd-27db-3aca-a3bc-278d7c27fb9e | -20.18571 | -46.48362 | 2026-03-02 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a4b0cd3-9874-3f7d-a3b9-6efab7c3481b | -20.19245 | -46.48049 | 2026-03-02 03:34:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56cda836-620c-3bf7-af77-ca9aa895a8bb | -23.61104 | -46.5351 | 2026-03-02 03:36:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93e74a63-5d60-3889-86e7-948fd5f8e8a0 | -24.33244 | -49.73054 | 2026-03-02 03:36:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b50f537c-8d5a-34b3-8f72-5cbde6128b0d | -21.09684 | -48.74347 | 2026-03-02 03:36:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 63310116-992a-3566-b6a9-80763b17d3a3 | 1.4864 | -59.9117 | 2026-03-02 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 34e2f7e0-7a27-3297-b3df-d5bafff996a1 | 1.5046 | -59.9306 | 2026-03-02 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7e6abaac-9911-3a21-a358-52b0a3e0178a | 1.5047 | -59.9116 | 2026-03-02 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 023a661d-ef62-376a-9f99-7c986537790a | 1.5047 | -59.9116 | 2026-03-02 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 1ff8c754-879c-3ef0-b076-52f7b2d13dff | 1.5046 | -59.9306 | 2026-03-02 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7df1569d-4023-3c38-ae1f-760b55c15525 | 1.4864 | -59.9117 | 2026-03-02 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 28aa365a-988f-3114-b8cd-9d039db53161 | 1.5046 | -59.9306 | 2026-03-02 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 2cb08dd7-39cd-3489-83e8-f25ed0aa8abc | 1.4864 | -59.9117 | 2026-03-02 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6aea59bf-9eaf-3e85-9caa-767d092f734e | 1.5047 | -59.9116 | 2026-03-02 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.9 |
| c731c979-1c1b-38ef-929a-2ef769693f01 | -9.54763 | -37.17923 | 2026-03-02 04:01:00 | NPP-375D | OLIVENÇA | ALAGOAS | Brasil | 2706000 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 837a3fc9-9a8b-3e21-a415-c6cfe2201b28 | -10.08555 | -37.67406 | 2026-03-02 04:01:00 | NPP-375D | MONTE ALEGRE DE SERGIPE | SERGIPE | Brasil | 2804201 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 90d16ea7-5899-3336-ba38-663c069a43cf | -20.18823 | -46.48393 | 2026-03-02 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| da55a489-dba6-38be-aae2-35a4177cc5b9 | -20.18681 | -46.48507 | 2026-03-02 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e948a5f0-14ac-33bf-8e17-8ccf7d1ada2b | -20.18431 | -46.48318 | 2026-03-02 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1ad51f41-8eac-3818-bdd3-2d1b73aaae43 | -24.33111 | -49.72675 | 2026-03-02 04:06:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a7e80d3-d008-3a9e-914d-d9c1cfda8a8a | -23.61246 | -46.53569 | 2026-03-02 04:06:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0091d858-af50-3d38-97cd-b8f1dcc8cc0c | -24.33018 | -49.73132 | 2026-03-02 04:06:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eec5503c-580c-36f8-88a4-8840d8efbee4 | -24.33553 | -49.72773 | 2026-03-02 04:06:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40c68a6b-8c37-3866-af4c-d24f2dcedae4 | -23.61618 | -46.53649 | 2026-03-02 04:06:00 | NPP-375D | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b40a426d-1a0e-32ff-84a8-648d301049f8 | -21.37935 | -48.64019 | 2026-03-02 04:06:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34d3e801-9e75-37ec-9703-bfa82e4a5c7d | -21.09372 | -48.74709 | 2026-03-02 04:06:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ef627226-591a-3956-9351-0a404e6210e7 | -21.91284 | -49.44827 | 2026-03-02 04:06:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a84c13f9-eb9f-335e-9668-00f9403d8c68 | -21.91184 | -49.44673 | 2026-03-02 04:06:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b8e672c7-2adf-36ea-b837-4e95a7ffda0a | -30.10825 | -52.67407 | 2026-03-02 04:08:00 | NPP-375D | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6a4d2447-c3b3-34de-9962-15f0d9bd70b1 | -27.85012 | -48.60281 | 2026-03-02 04:08:00 | NPP-375D | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 73ae7145-eead-3537-8b2a-142450609b8d | -27.84992 | -48.60305 | 2026-03-02 04:08:00 | NPP-375D | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cf1fdea1-b6bb-3f5a-929c-2d34716169e1 | -27.61167 | -48.66216 | 2026-03-02 04:08:00 | NPP-375D | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fa00a5f4-8e53-3722-8c81-55d7bdc1dee5 | 1.5047 | -59.9116 | 2026-03-02 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.5 |
| cb245846-767d-314a-9e8b-4afd9ac1557f | 1.5046 | -59.9306 | 2026-03-02 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5a199275-3b37-3a00-be22-c767a479119a | 1.4864 | -59.9117 | 2026-03-02 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b2b07880-caf0-392e-92ff-adedd933b6e7 | 1.5046 | -59.9306 | 2026-03-02 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e6b96d27-be69-33cf-8d55-df880aaf741d | 1.5047 | -59.9116 | 2026-03-02 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 8db7e98e-35c1-3097-8030-c0eb742572cb | -21.09301 | -48.74485 | 2026-03-02 04:25:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 87f1d908-7d7e-32e9-b44d-c86d0becbc2a | -21.30481 | -48.58892 | 2026-03-02 04:25:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)

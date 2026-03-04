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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d314183b-def9-3a28-9101-3aefe2a636de | 1.1107 | -59.19673 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6857e09-7828-3eda-a7d2-04844e21a25c | 0.27455 | -60.62387 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c30c7fd6-4505-3402-9d39-7787427eafa0 | 2.91743 | -60.45626 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28674207-2c0c-321d-8ccd-e7d3ae737ac8 | 3.03012 | -60.64869 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 660d0e45-38d4-33ba-940c-fd2490e2d853 | 1.51602 | -59.93523 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8afec31-3db0-3bcc-80cc-0c680154c170 | 4.04877 | -59.86699 | 2026-03-04 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a152f3e2-5faa-3887-ae52-4da7dc903661 | 1.49839 | -59.91662 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff37b622-ee2f-38af-a9d3-b9e9fd3a5e1e | 0.0577 | -60.99287 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 762cbbbc-043c-3ef7-a700-0ed50de2e703 | 0.27365 | -60.61837 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dfceaba5-facc-305f-800b-ceb5160218bf | 0.04025 | -60.98068 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ed5a9377-f7fd-3107-865b-92046e809de1 | 1.21066 | -59.97828 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f10a87b2-5db6-3971-9e75-cb1c22cc0991 | 1.50875 | -59.92011 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a10703e3-8aeb-3b6a-a43c-9234efd684ac | 1.05935 | -59.49198 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4076362f-3100-35a3-8852-000cd50e6bb7 | 0.45755 | -60.39712 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58071baa-4967-3667-98d2-13d7e7a24bbe | 1.50793 | -59.9148 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 64f12d11-0c0f-3c89-82fb-c92b4e1ff16c | 1.21547 | -59.97762 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83f90acc-11fb-305c-a65c-6359d559814a | 3.04045 | -60.64712 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bb9d487-b0c6-3ff6-90af-6ae534185c1e | 3.05646 | -60.64135 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 767927f0-8d7f-3dd2-8abf-67001042f8ab | 1.11243 | -59.20398 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a460654-5fd3-333d-acbd-cf4734649636 | 0.05265 | -60.99371 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 53666c53-455b-31f8-b31c-bdaca6ab2409 | 1.15387 | -60.88147 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4cc1fd5-1687-3975-b8ac-d562279f419b | 0.45842 | -60.4025 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60e05e1d-e345-3658-9992-8a931d705002 | 2.22781 | -60.75048 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ac8d7f3-b65d-3fe1-9ce7-0b07f557e8a7 | 2.67313 | -60.41633 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 415d253f-bb5e-3771-ac7f-feb8f1cf925b | 1.0093 | -59.50484 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fe207d5-d7d1-31c0-9beb-4e0d3f1f87b7 | 0.05817 | -60.99589 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 695dce58-9a88-3d71-af70-027a5a497fa2 | 2.64129 | -60.44517 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 184ffde6-3f8d-3b1c-8b4e-66f2d46b4984 | 1.0601 | -59.49667 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e03e9a0-4dc9-3be1-a6b8-e0823bebc577 | 3.8771 | -61.68851 | 2026-03-04 05:01:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31bc489e-59eb-38d7-8327-762bf1523192 | 0.73609 | -59.9098 | 2026-03-04 05:01:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6944517-c138-3ce7-a00d-a2d4c99e5910 | 0.04987 | -60.9761 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 000034e2-843d-3f58-9411-17e04af1065b | 1.06258 | -59.48922 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab7c8ed7-c5dd-39ca-b29d-71267c95a60f | 0.94836 | -59.44675 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 836150ae-eb26-3ace-b77c-c54164bf41cf | 2.66808 | -60.41711 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3137b01-c1b0-37bb-9bd3-e23960c17e1c | 0.04485 | -60.97702 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 84d0af5d-37f4-31ec-8486-edd02bec4858 | 1.51186 | -59.90853 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 49388024-8be9-3506-abb4-16fac93e3c6a | 1.11143 | -59.20127 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3675afd2-f2ba-3569-87f6-8fdc0ffc6792 | 0.04715 | -60.99161 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe9d6232-8581-3168-a0a0-fa4e7947c359 | 2.66763 | -60.41418 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e5fbf2a-e241-3ce9-aa00-68e9b83b0f3e | 3.05547 | -60.6417 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17d2c910-6675-3234-ac25-5fbf35ba87be | 0.73531 | -59.9048 | 2026-03-04 05:01:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5fe1096-5da7-338a-a3e5-d1b268188caf | 0.48766 | -60.51203 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a705ea87-1d4a-3638-a77c-eca8198a3ca6 | 0.49834 | -60.51588 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f652fedd-cd9f-385f-8594-be1531f94e22 | 0.27858 | -60.61755 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53e39b71-05db-3bd2-9458-fd706a269f41 | 1.50317 | -59.91576 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0aa940e-d186-3b0c-a5e7-45771e7869ae | 1.0356 | -59.46173 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8320f5fd-d6bf-3a00-b978-dafe2fa9cc15 | 1.15533 | -60.87475 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4158244e-b2eb-3b31-9e5a-b6f464405b94 | 3.04614 | -60.64294 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea6480a4-4e04-3385-9c26-57f2b47c0e5e | 0.05123 | -60.9847 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| b03058c0-0016-376f-9b32-7a2a4d7ed252 | 0.0453 | -60.9799 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| b754dd46-1b2d-3f5e-b6da-9d71a140a9f3 | 0.45451 | -60.39484 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c559ff5c-fce7-39ba-8b06-1281edc35915 | 3.02073 | -60.6564 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfa6b5c5-b4b9-3d45-a311-425ca16bfbdc | 0.05031 | -60.9789 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 2de74d70-5bf2-3958-b2f2-4a41f89127a6 | 0.05077 | -60.98178 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 27.3 |
| b6435b5d-5bc7-3d79-b7a6-76162d96c995 | 0.04622 | -60.98571 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| d093f53a-a983-3776-a492-a0eb41487474 | 1.06396 | -59.49121 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c37d36-af27-3643-9e96-b8e405d01c56 | 0.27514 | -60.62308 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94fd6ef9-42b9-32e3-982d-6da45e6dbe3a | 0.05446 | -60.97245 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b950c6ff-cca4-3c7e-95ab-d922e3e22974 | 1.34841 | -60.02169 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a620da0-1b9d-339f-84c9-de8bfd6930d8 | 0.30352 | -60.45071 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dc40a44-cbbe-3262-952d-cc15f30bf2c6 | 4.64653 | -60.69822 | 2026-03-04 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a08a29c4-623b-3775-95d0-acacad4a4f0a | 0.71436 | -51.37187 | 2026-03-04 05:01:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c3b3c7-c7c7-3629-af7b-23132cc06085 | 0.64878 | -60.37363 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f322941-4adf-3900-adb4-aef555e6fe81 | 1.10721 | -59.20015 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac3add02-df13-3b93-b50a-c00c1aa526ff | 1.1585 | -60.87771 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34d0f852-da16-3f2c-b76e-5a93f23ca378 | 2.9256 | -60.46203 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eaf2eac5-215e-3a50-967e-6cf90a93d197 | 0.96241 | -60.24065 | 2026-03-04 05:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b56f821-0f6e-3821-898d-d7e0bfc9c581 | 0.95296 | -59.44599 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9028fea-81b7-339c-8f68-a4a1311c204b | 1.02182 | -59.8013 | 2026-03-04 05:01:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfa35042-7eea-3ee3-a6b5-e1b0f4cc127a | 2.91787 | -60.45924 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e22bd54-e0c6-33c4-9e97-58d6b3b1d2a0 | 0.94894 | -59.44369 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48c040ba-4a75-3184-83ad-d816fb07fab6 | 0.05626 | -60.98384 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79d447a3-ca5b-3f11-9b9d-0154b8a4a128 | 2.65754 | -60.11001 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffd0a7d5-e12e-3142-81d4-db810b862fbb | -0.15307 | -60.76032 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d881ac89-0fa0-3d1d-a949-6d79d316e482 | 1.08162 | -59.24807 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be137f6-7427-32a4-a4c7-c6aa364a5bb7 | 1.11627 | -59.19871 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5de4e41-4aa0-384e-8393-6b3d1b1ca959 | 3.01602 | -60.66026 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45c7ce35-70a9-3064-94a7-077706377a16 | 2.65178 | -60.10523 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5573e515-b76b-3272-bb86-1a5fa6f89569 | 0.92581 | -60.53866 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 056876a8-a610-3bda-841d-b76e27a540ca | 0.31242 | -60.44375 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a96f1505-a394-3b75-b228-b58215c573f4 | 0.92033 | -60.43779 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53d8b251-831a-32e1-9ee9-85f116718b3b | 0.27428 | -60.61755 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ddbcee4-2e30-3f3d-b5a2-6ef8d0c64612 | 1.0633 | -59.49393 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5478bc36-78d8-3b1d-9efd-ce17d5ac9b1d | 0.04258 | -60.99546 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 86e688b7-5e98-32a4-a9ca-3c17c6f202f6 | 1.5527 | -60.39884 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2fa0396-f327-3a4f-abc8-c2a7e1ccf07e | 2.67863 | -60.41846 | 2026-03-04 05:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8762876-ca86-3a92-9a74-e7a883ef377a | 0.96072 | -60.22955 | 2026-03-04 05:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4be25578-0816-3e3a-9044-0ad60d99006a | 1.15803 | -60.87474 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a02661d7-1cb1-347e-8614-2b786b4926d5 | 2.90974 | -60.43923 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04489db-9c08-3769-9340-76448680d771 | 1.15578 | -60.87773 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e91cc6e7-b605-35d0-8a03-41e38f139489 | 0.30754 | -60.44454 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b730c6b-8073-3c2c-ac59-3994a87cb2bf | -0.15283 | -60.75955 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a750765-2653-3dc7-943c-405647c9b7ac | 4.64129 | -60.69946 | 2026-03-04 05:01:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8903062-c67e-34a7-9b17-2328b865da8a | 2.6616 | -60.11082 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da2862c0-bca1-3e29-b7a0-e5e4d8113f02 | 0.27948 | -60.62303 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5adc7716-3b7e-3e56-9ed2-baa246e76c39 | 0.04943 | -60.97332 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ed259bd-b0d4-3472-887a-a813ff569466 | 2.65579 | -60.10603 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2c67101-107a-3a19-8c6f-82c4c39deade | 0.49172 | -60.5057 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a33a66d7-58ed-36e6-a62d-b4bde2aadd28 | 2.9093 | -60.43626 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 955dca76-bbf1-333b-bb49-515579acea7c | 0.16897 | -60.59536 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)

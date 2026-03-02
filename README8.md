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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bbbfb71-28b7-332e-b3a0-dc63e7e50b00 | 4.07428 | -60.3353 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7543b6d8-9742-3d7f-a4fd-bb1599bc2d57 | 1.49162 | -59.92779 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afdc33cd-eab1-319b-8de6-fba6eb88e1e3 | 1.48758 | -59.92458 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f53bb280-0ad8-30b1-b5c0-27087e660b8a | 2.85927 | -60.80994 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| add9c44c-43e9-3178-934a-c2d49506eaf8 | 0.71183 | -59.51603 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c2610a-2fc1-38d4-a050-5d84860f9381 | 4.2551 | -59.90604 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a0b3048-d07c-3b4d-bb9c-9d22ea9cda7f | 0.89587 | -60.09086 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4a5e727d-38a9-35be-84f7-fcbd789a40e0 | 4.25673 | -59.89463 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c87bd0d-5b7e-3e25-9b31-c9fd73b14cd7 | 3.18152 | -60.68776 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bc0214f-92b4-3518-8814-0f0fe17df93c | 2.85983 | -60.81344 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60feeba6-96ec-3adf-9a92-9640dfb2d4ed | 3.42626 | -60.82108 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d6ae426-78e9-3c87-ab8d-fd224726b06d | 1.50078 | -59.91866 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 974748aa-c59b-3aac-8e4e-097849c12f6f | 1.50305 | -59.91068 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b06bb6fb-0905-3a13-a613-6e536ab25e85 | 0.09792 | -60.63056 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e8ae8d7-b49d-3906-b464-844aa0eeddad | 1.86379 | -60.40314 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 353254eb-d642-3bf5-9637-32fe7abc2bce | 1.0243 | -59.80195 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3c44cbe-87ed-3411-8fb0-69d16ab4367c | 1.73563 | -60.386 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bcdca3c-aee8-3a4a-a2b6-6352ad963b6c | 1.50019 | -59.91493 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aac5fd87-f4d6-37c8-be8a-2a2761a76783 | 0.49098 | -60.51067 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cb42136-7c9f-3c0b-864e-54bdb0e3acc6 | 1.49674 | -59.91545 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 185454b8-2bc1-3abe-93d0-b838684bd1f2 | 3.16497 | -59.90799 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e57465c1-0540-3fed-bdc5-8bd64edbf164 | 0.91973 | -60.53091 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52b33acd-9071-33a3-b6af-160bcf3c44ce | 3.02044 | -60.6916 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1610cef7-b277-3635-a29e-6a742dbc0aa9 | 4.506 | -60.54095 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22172c19-7fd0-3b7b-970d-b61809cc5a5a | 4.37325 | -60.62193 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e33e7c2-c01f-3f93-a4ea-1fa5261fccc2 | 0.67574 | -59.5607 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f214258c-4908-314f-8fca-07fe0a022339 | 0.65561 | -59.61591 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f41f2b74-4acd-39b8-b1b0-d8a533e60b90 | 4.25731 | -59.89827 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1d6d060-419f-3c12-b069-73b0608c9dc2 | 2.85241 | -60.82533 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c479706f-0c42-3416-b1c8-85cf130c6142 | 1.50196 | -59.92618 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 259f0656-21d8-33ba-89e3-4f3b9878c5ee | 2.2235 | -60.74815 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b545da45-19f8-3256-a60b-b0161b313fb5 | 2.67725 | -60.42326 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ca230c0-54a3-318c-b6b3-21bddd8d3d92 | 1.4927 | -59.91225 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0cc934ee-17f2-319d-845c-5964cdafdbd6 | 3.42071 | -60.8291 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7482b78-f4f6-3ccb-b007-1f78c3d04f42 | 1.74259 | -60.25499 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eff31ec1-3240-368e-8363-ba1491ab1e78 | 1.07495 | -59.25463 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37ebb0a9-7dbd-33cf-a5f6-e7204758e8c9 | 4.06432 | -59.8946 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8a22bae-777a-3c74-b4a5-fe19f2e3b292 | 2.86262 | -60.83091 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48217443-5777-37f1-9ead-e534b09502f6 | 0.09102 | -60.56443 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09ad3185-f2b5-39ac-b6ad-e6f5840f54a3 | 0.11495 | -60.62791 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4b17989-7e56-3bbe-b286-fe02c7cf7bc3 | 1.506 | -59.92939 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50811253-1cb5-3921-b285-a6d806dbf9bf | 3.17818 | -60.68832 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3644cc3-abc4-3fa0-b8d7-5ebfc2fad138 | 3.19709 | -60.67803 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e067ab22-d3ff-3dd4-afc2-6d07bf18d324 | 1.02247 | -60.54116 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f12ba81-31e2-3b8e-bd73-5a6ecb96537d | 0.46163 | -60.39159 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa30469d-c33f-3afd-a109-f1dc6020d6c9 | 1.20352 | -60.61997 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92efe187-3298-3c26-a6d8-15d92f5113a2 | 3.41404 | -60.83015 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4543f790-e4be-38d0-bccd-e83920ef22cf | 1.8666 | -60.399 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 119a7c7a-5a42-3fa5-9ff5-6b23ab89970b | 2.85984 | -60.83493 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6513656-1753-33d9-9c94-c098e97e4989 | 4.3788 | -60.6139 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0187d4f2-b68f-3732-99b3-3902d61dbbc4 | 3.60989 | -61.65654 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6d9f6fd-4845-3846-8faf-0239767ebf12 | 0.09566 | -60.63835 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe232773-904c-30c6-b187-bdbe892a8732 | 0.37164 | -60.37498 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6beb17f-4e61-3caa-bf52-802cc7faf0be | 0.09054 | -60.62798 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f7ba0cb-5d11-3ef9-a04a-193d01170601 | 1.48936 | -59.93584 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31faa689-9afc-3de0-9035-1167c4135fbc | 1.49043 | -59.92027 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 600b4e2e-36cf-3d50-8a6e-93b7b9b72bf9 | 1.47664 | -59.92247 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ea9cfd4-28c9-381d-9ea0-518e3afe3a2b | 1.09856 | -60.18169 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 10fe9748-125a-3634-9318-6f312e832a21 | 4.60131 | -60.75735 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44b8a014-1276-3f2a-b2d0-ef514ba3c434 | 4.2579 | -59.90189 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a481c788-3fce-36da-8e23-df058b60a9e0 | 1.12034 | -59.20272 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df9189a6-c4cb-37fa-ac8f-4e0c117607b8 | 1.50709 | -59.91391 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fe75f35b-73c7-3ea9-98f4-4d2bc3d40a2e | 3.16896 | -59.9111 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 563d7395-55f9-38ec-9b81-d6e62010db21 | 1.06008 | -59.25286 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b38f6c3-57e9-3c98-b85e-7bf37180ff27 | 1.16381 | -60.83414 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a82220b3-fef8-32f6-84d1-f773ce9fa1db | 1.51575 | -59.924 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 757e2b26-88b7-3555-bd16-88cc64eadd39 | 1.11549 | -59.19526 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33ad3e73-60a0-3794-bc81-0684a5ac53e1 | 1.51061 | -59.93623 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd3f67d-ed84-30cb-a003-6d2939e8c9dc | 3.41682 | -60.82614 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93351163-c1c7-3e61-a1e8-effbbc2f9560 | 1.2069 | -60.61944 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64dfe400-fc06-3eb8-bed4-5bec8f71fb41 | 0.6476 | -60.66494 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a6a9390-8161-397b-920f-642931197676 | 1.48473 | -59.92889 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e8b480d-a448-3355-9ed1-2ab9d0a6e994 | 2.8615 | -60.82393 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf01325c-667c-36ff-bcc8-71f02cd5b18f | 1.16941 | -60.826 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00790efc-9381-3fb3-873b-4882e1a7b23d | 1.11385 | -59.20788 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cc88b2b-ac6c-3f86-be27-34e92cc5ec06 | 1.09739 | -60.17429 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e145d096-e9ba-3279-af27-3c12a0c07efc | 0.36822 | -60.37551 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af8c5aac-ab89-3bd0-94e4-1705cfd5b774 | 3.0566 | -60.66798 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a39017bb-baa5-3692-b582-a4c9f054ab1b | 3.04991 | -60.66903 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ae19faf-d0fc-3450-ac33-4bd16f7ac522 | 3.01487 | -60.69967 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 122fc468-a33f-3611-b55b-b60a31bd0d35 | 1.86717 | -60.4026 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66ed1ed4-84bb-3180-bbfe-198c61cb808a | 1.85983 | -60.40007 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 588756a6-ca84-39f6-9ad6-63296d2614a1 | 0.44971 | -60.40475 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48b16467-7286-3166-8001-b292e931f5af | 0.92313 | -60.53037 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f72d729b-5236-3a39-b717-842b1e33e909 | 4.17342 | -59.79219 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62481703-5d27-3c6f-bb89-cdb4371a1d64 | 0.64365 | -60.66187 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c5a3937-c9cd-3a4a-b2b3-173a8f5cfb01 | 0.31256 | -60.44449 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f309f76-6e1e-3499-8da7-77c328be5f26 | 1.72118 | -60.2956 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 464bb7c5-a092-376e-a88b-3a98bf282113 | 0.49837 | -60.51325 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9178cc4-891c-3917-a69e-f910d54c7608 | 3.41904 | -60.84007 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd1290e0-267c-30a1-a8e1-e317739276c7 | 1.48984 | -59.91652 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7ba8170f-66c9-39ec-9de6-5a029ab61006 | 2.86151 | -60.84541 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adc0c361-d5ef-36b1-9ce2-1b2551e98582 | 0.47306 | -60.39734 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 900b4437-276f-3cb8-ab8a-44572bc6ee47 | 2.11642 | -60.80104 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2852f3cd-3c22-3fb9-b605-c2766e5fb6d0 | 1.50717 | -59.9368 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0677dbbb-ce0e-3a7c-b160-7997f7eaf521 | 0.49496 | -60.51377 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 487b18fa-a1f1-3dd1-a8a7-b6fbde8cd9e9 | 4.25615 | -59.89101 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b38f5ea-ae85-36b8-bc51-950125d534a4 | 3.04497 | -60.67336 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afe3f2fb-d59c-306a-a9e6-89c83fe358dc | 0.70191 | -59.97427 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f07316c-64c6-3432-b8d2-86ec517d9412 | 4.0649 | -59.89819 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README9.md)

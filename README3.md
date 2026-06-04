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
| d42d4f43-60c1-3df7-9b88-65eb292c97d2 | -12.2517 | -57.2656 | 2026-06-04 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 05d3e9bb-5cc5-38dc-9240-b5eee548f974 | -10.3842 | -49.4338 | 2026-06-04 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 72b34e4a-8e39-3f60-b5f5-cb4b2e172aff | -10.3842 | -49.4338 | 2026-06-04 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 5303ccd2-f6c0-3035-92aa-a0eddedb54aa | -3.9867 | -47.9326 | 2026-06-04 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a233a394-7c23-380d-b080-70fa8041bacf | -11.5688 | -52.7848 | 2026-06-04 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| aebfd93c-945b-341c-915c-b695e1c3dc60 | -11.5309 | -52.7887 | 2026-06-04 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a498848b-9c9e-36be-b060-6f049990b45b | -21.5657 | -48.5878 | 2026-06-04 01:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 68.0 |
| baf84bb8-ad21-3d59-aecc-d0d6c7a5e7f4 | -12.4654 | -58.481 | 2026-06-04 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 55067501-e0cd-34b5-8e4b-5938764179af | -12.4656 | -58.4612 | 2026-06-04 01:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ae1af13d-e60d-3a62-abff-d669330fda53 | -11.5499 | -52.7867 | 2026-06-04 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 2272bb2f-66ff-3e8c-ba90-e05b0d0efd67 | -11.5499 | -52.7867 | 2026-06-04 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 2909eff7-d6c8-3255-9c9d-550f6f7bb518 | -11.5309 | -52.7887 | 2026-06-04 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ad7d7c7d-5b18-393a-bd21-dd2979676980 | -11.5688 | -52.7848 | 2026-06-04 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b33ee615-ada6-35af-961e-34290db67717 | -12.4654 | -58.481 | 2026-06-04 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| ae7057f1-0e2f-3a89-9837-0c6b845a0146 | -12.4656 | -58.4612 | 2026-06-04 01:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 69856ceb-9d0e-384d-b83a-14c592a1eb71 | -16.18975 | -58.4603 | 2026-06-04 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.1 |
| 3d801421-8b1e-31c6-90cb-08096e7add8f | -16.19444 | -58.48626 | 2026-06-04 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.9 |
| ee1efba5-50a3-3aad-b436-d4fb7858fb5c | -16.12063 | -58.50663 | 2026-06-04 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 336d124a-f7cd-3a09-aaae-f74e182fc0d6 | -16.18687 | -58.46644 | 2026-06-04 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.1 |
| e08664e8-3c21-3892-a8f0-3503609e0eea | -14.09737 | -59.37828 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 19ca8369-d241-3581-9abb-095ea0c665fd | -12.46867 | -58.49678 | 2026-06-04 01:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 5f9eb226-300d-3b0f-ab25-70aa83144dbc | -14.09207 | -59.3851 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8f07329a-35ec-3427-a236-3bd17e77508c | -12.20191 | -57.29658 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 63825ffd-842c-35f8-b488-f0b2f0eeec58 | -12.21595 | -57.24734 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 0ce332e4-9130-3cac-ba0c-9c2ee0198bb4 | -12.43752 | -58.40789 | 2026-06-04 01:26:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| f34d8ff9-fee7-339d-b0a1-35baf485e7d4 | -12.46516 | -58.49205 | 2026-06-04 01:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2f99cf4d-d7f5-3083-9195-3cae2895968e | -12.23275 | -57.24435 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 750f40d3-4597-3b43-94df-e8086f24ec3a | -12.23954 | -57.28248 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 96852e8d-6b7f-3a98-8c5b-f6e44b96a137 | -12.46339 | -58.46609 | 2026-06-04 01:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| dd217be9-5e16-30ff-a602-8e1822a862c3 | -12.2186 | -57.29328 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 550.6 |
| 16ec277f-c415-3041-b09e-ccace58e9424 | -12.21198 | -57.25496 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 392.0 |
| 3aeda085-a287-3f1f-9485-c6df432f28ca | -12.44812 | -58.46894 | 2026-06-04 01:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 2344d99b-b2f4-3481-84cb-3ab796cf518f | -12.20612 | -57.28884 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 7aa698d4-3e9b-33ab-a2a3-1f8cc9b87665 | -12.22282 | -57.28559 | 2026-06-04 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 969.1 |
| d2262ed8-02f3-3205-b470-9f82f0da2bab | -12.45962 | -58.46122 | 2026-06-04 01:26:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 293fd5fe-817a-35ee-ad51-00df3c72ba81 | -7.9419 | -71.45897 | 2026-06-04 01:28:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 04d590cd-ab02-3b8b-b07a-f1c2de3bc925 | -23.4409 | -47.7856 | 2026-06-04 01:30:00 | GOES-19 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| 65970767-1cd1-3876-8b39-4d9bfbe334a6 | -12.4656 | -58.4612 | 2026-06-04 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 1ac058e7-7feb-3b4a-ad1a-f6f7b4484191 | -11.5499 | -52.7867 | 2026-06-04 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 48ef46a3-c672-3a11-8d69-5b1d5a66a14e | -10.3839 | -49.4554 | 2026-06-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 8ceb91b1-432c-33d4-ab64-40a8218553e5 | -12.4654 | -58.481 | 2026-06-04 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| cf9f0819-42a8-3586-a2c7-c9ed7862da41 | -11.5688 | -52.7848 | 2026-06-04 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8a11f0c9-7636-3bd8-a29b-3e0f9bf87163 | -23.4401 | -47.8097 | 2026-06-04 01:30:00 | GOES-19 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| bfee1957-c15a-3bcf-b26b-a8292f607f3a | -11.5499 | -52.7867 | 2026-06-04 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 110638ab-124d-3aed-aea6-65fc88c84823 | -12.4656 | -58.4612 | 2026-06-04 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| c7ab869a-cac3-3e0d-aff1-96e5a9edec3f | -10.3842 | -49.4338 | 2026-06-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a22165fa-c116-3d96-b188-b53e3aaaecfb | -12.4654 | -58.481 | 2026-06-04 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 9c3a5361-4e72-3d94-89ee-7cacef650475 | -10.3839 | -49.4554 | 2026-06-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 41fc1326-291e-3e15-ae4a-2304271d4d88 | -12.4656 | -58.4612 | 2026-06-04 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 89de0cbd-51ce-38de-a368-07e241562e67 | -11.5499 | -52.7867 | 2026-06-04 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 30b4a705-5e5c-39e5-a763-c955fc1bbafa | -12.4654 | -58.481 | 2026-06-04 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f69ce75e-6611-3791-b7c5-4157aae2f40a | -10.3839 | -49.4554 | 2026-06-04 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| bfb57e8d-163f-33a0-8306-3d4ab95f8a3d | -11.5309 | -52.7887 | 2026-06-04 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a515c7ed-d44f-3561-94fd-15123ee9703d | -10.3839 | -49.4554 | 2026-06-04 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 30853231-3681-306b-ae61-031fb4d69402 | -12.4654 | -58.481 | 2026-06-04 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f5e2ab25-a7e6-3d60-85a4-5a5714f10882 | -12.4656 | -58.4612 | 2026-06-04 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 42d8c307-b640-3a48-8c01-2722397333f3 | -11.5499 | -52.7867 | 2026-06-04 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 842493a6-7f36-352e-80f2-5cd31aeef8de | -10.3842 | -49.4338 | 2026-06-04 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d323e5fa-dc3f-37e8-ad59-0ec8cff3b210 | -11.5499 | -52.7867 | 2026-06-04 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 0f592550-0c5a-3ef5-a5d4-3c4234f95167 | -12.4656 | -58.4612 | 2026-06-04 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 208c9ba5-9699-35d6-9ed3-67ebca011cc8 | -10.3839 | -49.4554 | 2026-06-04 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| aac5adb5-0543-31f9-9760-5f8a4c739ad1 | -12.4654 | -58.481 | 2026-06-04 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| fee2b237-f482-3bff-a3cb-2649f19feae0 | -12.4654 | -58.481 | 2026-06-04 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| f88e1303-e10c-3c4e-8857-019b9f2f0a02 | -11.5499 | -52.7867 | 2026-06-04 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 5da560fe-16a9-3481-98ca-187c0927f483 | -12.4656 | -58.4612 | 2026-06-04 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 4851e750-28ed-3e74-aa5b-6790b2899772 | -10.3839 | -49.4554 | 2026-06-04 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d9f0423a-fcd3-339a-9f88-49525e4a98d6 | -10.3842 | -49.4338 | 2026-06-04 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 1e6e70bc-72f7-3a96-af44-a8fad95e4d3f | -12.4654 | -58.481 | 2026-06-04 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 5d87d0f7-aefb-39f3-8d92-6bd4d57199dd | -11.5499 | -52.7867 | 2026-06-04 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 3c77d4ed-6a12-37cd-9cdf-a25ac10479e5 | -10.3842 | -49.4338 | 2026-06-04 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 841780d8-79b0-32fa-ad56-583645f98230 | -10.3839 | -49.4554 | 2026-06-04 02:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c772022d-590c-37c7-ab95-e199362ebe75 | -10.3842 | -49.4338 | 2026-06-04 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| a9df605a-f4c7-30f5-88f3-15304a8c634f | -12.4656 | -58.4612 | 2026-06-04 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 3af1e84d-0af3-3795-adf9-3e7d95aaef81 | -11.5499 | -52.7867 | 2026-06-04 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 4b643b3a-a478-35df-92d8-1cd045f50d73 | -10.3839 | -49.4554 | 2026-06-04 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f84248cf-99b8-3286-b376-83c87fb652d8 | -12.4654 | -58.481 | 2026-06-04 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 323ddf13-b4b1-36d1-8929-64e4de8f36cf | -11.5499 | -52.7867 | 2026-06-04 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 275c2d56-790a-39d5-8e73-76237c7cb001 | -3.9867 | -47.9326 | 2026-06-04 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d1038cad-cb2a-3c21-96e5-69751359f8bc | -10.3839 | -49.4554 | 2026-06-04 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d61974eb-4fe7-35fd-b304-4f0ab58916d9 | -12.2136 | -57.2888 | 2026-06-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 991.3 |
| adcd626e-c2fa-331e-ad2d-ff428d7162c1 | -12.2138 | -57.2688 | 2026-06-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 447.4 |
| 1c518d25-e0ff-3199-8c8b-474e9b83a286 | -3.9867 | -47.9326 | 2026-06-04 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| de90d5c5-8203-3f0b-969e-2d2a1852be0d | -12.2133 | -57.3088 | 2026-06-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 6525d0b6-8465-37e7-8a8d-71255cb2559e | -12.1946 | -57.2904 | 2026-06-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| d1cffc93-40cc-3f8b-920f-01548b33c428 | -10.3842 | -49.4338 | 2026-06-04 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6575e534-9795-3b57-8776-dc7f07295003 | -11.5499 | -52.7867 | 2026-06-04 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 25281636-1881-3bc2-95d1-d1b4d8a3a49c | -12.2327 | -57.2672 | 2026-06-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 561.3 |
| 1527f097-c741-3932-9f19-5d04d305e8c7 | -12.2325 | -57.2872 | 2026-06-04 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 687.6 |
| 36cddf62-41d6-3626-acaf-dfded7d44403 | -12.2138 | -57.2688 | 2026-06-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 488.3 |
| 08efc7a5-fa34-35cd-82cb-7623d862130a | -10.3842 | -49.4338 | 2026-06-04 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| dfeba1ca-79bb-3b35-bc24-3cd13b6ab95c | -12.1946 | -57.2904 | 2026-06-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| f7d9ad99-d43c-3ebc-bb8d-aaee59e6451a | -12.2136 | -57.2888 | 2026-06-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 748.9 |
| 81048547-be9f-3979-a58e-d131833a058f | -12.2133 | -57.3088 | 2026-06-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7b750ae7-64ab-3f2e-89df-94100b5607ea | -12.2325 | -57.2872 | 2026-06-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 526.3 |
| 46264a56-d4fa-39cb-ba4d-7646fcf9fe3c | -3.9867 | -47.9326 | 2026-06-04 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f2499b76-40cc-35e8-8d7c-f50140e8a584 | -11.5499 | -52.7867 | 2026-06-04 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7fc9b4b1-f193-398b-afc4-466fffac5f56 | -12.2327 | -57.2672 | 2026-06-04 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 438.1 |
| 56d5a523-38d7-3245-94af-fddb1d03e6d5 | -10.3839 | -49.4554 | 2026-06-04 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 8a91d5ec-b32e-3a2a-985e-fce37a17c33d | -12.4654 | -58.481 | 2026-06-04 03:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 8e93685b-e3c6-3001-9e17-fd359129f6d9 | -6.99071 | -42.874 | 2026-06-04 03:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README4.md)

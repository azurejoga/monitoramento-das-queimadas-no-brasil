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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ffa10b6-1581-3daa-8ac1-f00d55564047 | -4.28698 | -48.63477 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5efb5f11-476b-3f85-9e71-de44d6580438 | -4.27496 | -48.23271 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56298e8b-e967-3093-9610-b39045866756 | -4.27026 | -48.23206 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87ee43f0-f442-3019-b3b4-a99d248acfcd | -4.25455 | -48.65121 | 2024-10-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bc27a35-3dc9-3997-a4f8-b0c97b902fe9 | -4.11632 | -48.27531 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6084d535-d0ad-3ad9-a28b-f644f1f50c37 | -4.1159 | -48.24904 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a159836-f4d1-3d42-b4d6-67493aa72926 | -4.11506 | -48.25403 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 834caf8c-4d98-3c03-b727-b66c3a2a1612 | -4.11248 | -48.2694 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b46797c4-b6f6-35f7-86be-fc82f8d94fa3 | -4.11204 | -48.24333 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3e3e544-08e0-3629-8876-6c8b0cb57437 | -4.11076 | -48.27965 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d1a6f91-8f1d-3687-be8a-5f87548d5833 | -4.11037 | -48.25323 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5cfbfb3-8209-3eb0-8105-ae6313814107 | -4.10952 | -48.25832 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 973944e6-d3f7-3b37-bfdd-de342aad4c30 | -4.10865 | -48.26346 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a06ea48c-09e7-395f-8ea5-012e194ecc3c | -4.10778 | -48.26863 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e73c366-6d4f-3c87-a784-953870378809 | -4.10734 | -48.24259 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 436ff4ab-52d8-31d6-a43a-ef969ee5a4ce | -4.10652 | -48.24749 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef1f4690-1c0e-39b0-9ea1-85bf2da6dc12 | -4.10568 | -48.25246 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7095495d-4f1c-33aa-bee8-86ace857b855 | -4.10482 | -48.25755 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85d68593-802b-3e73-9c00-f3abdb2addc3 | -4.10098 | -48.25171 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7266947c-c25e-32fe-9e88-2e553f0126f9 | -4.09709 | -48.24618 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44b78599-b066-3f79-8ce6-38179a8b7630 | -4.09627 | -48.251 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1a05960-3765-3269-bb57-908982187e69 | -4.09533 | -48.24543 | 2024-10-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1d724e7-3b79-34ae-94d9-9a988e5d1784 | -6.4228 | -48.27039 | 2024-10-12 04:06:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4ef75122-b0fd-397b-84bf-53cc441846da | -6.42202 | -48.27499 | 2024-10-12 04:06:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ce44821a-1914-30e1-91b3-488954cec53a | -4.4197 | -54.90609 | 2024-10-12 04:06:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d695d38-e81d-34a8-89ce-83b29f8a6a31 | -4.41267 | -54.90429 | 2024-10-12 04:06:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a102e336-02d1-31d8-96fa-926520d8959f | -7.86183 | -54.69464 | 2024-10-12 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c915f56d-8248-358d-96e4-72c0d2c6cc59 | -7.86083 | -54.69992 | 2024-10-12 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1deb5935-ea56-35bf-9ec5-c8db13477ea5 | -7.85978 | -54.70545 | 2024-10-12 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a334e6f-78fd-3681-8e87-72d27fe4c6ff | -7.85404 | -54.69919 | 2024-10-12 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fbf3a5f-05ae-3593-8ee9-a6f0831bdcc6 | -6.41828 | -48.26958 | 2024-10-12 04:06:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f0292ef0-7585-347e-a98e-92a63b20f786 | -6.4175 | -48.27418 | 2024-10-12 04:06:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d1bebc12-f4ce-396d-99fd-62909d10c7c6 | -6.06959 | -49.13527 | 2024-10-12 04:06:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56cdd90f-62c2-31c0-8f5a-46db18154b16 | -5.72992 | -48.47126 | 2024-10-12 04:06:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 622d4bf2-4fce-32bd-ad2d-ded4406c4d97 | -5.50868 | -48.08477 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9fa4943-3d5d-32f8-abf7-b8893c88355d | -5.50788 | -48.08943 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dda5ca55-cb9b-31b0-b2c1-8c021ba2c304 | -5.50733 | -48.08625 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac3c97d1-aca6-3b60-992c-ed112508a916 | -5.50279 | -48.08549 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84e755d0-d5ea-35cc-a388-189e740f4c89 | -5.50202 | -48.09014 | 2024-10-12 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb43d943-9c3b-3a90-baa5-01da7888580d | -5.24707 | -48.04123 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 55f3822a-63ea-37ae-b586-50793633a697 | -5.24629 | -48.04586 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 77215219-f32a-3aec-8e92-47f13b5869a5 | -5.24253 | -48.04046 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef0f0d8-c2e6-312e-aad8-2c16fc15e225 | -5.24174 | -48.04509 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 875dede5-4425-360f-8f3f-bcd6dc0c7586 | -5.24097 | -48.0497 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ade72fec-ae18-3243-8841-cfd5d93fae07 | -5.196 | -48.17629 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9978c9ab-305b-372f-9ecb-defe36c2fea5 | -5.1952 | -48.181 | 2024-10-12 04:06:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1674066e-1778-309f-ad42-801869b34ecf | -9.18411 | -48.95355 | 2024-10-12 04:06:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb35ced8-535c-3b19-9d05-eff2cf6a34aa | -9.0296 | -48.81042 | 2024-10-12 04:06:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c54959cc-df91-3fe1-b49b-6744b73ef0f4 | -8.06604 | -49.77876 | 2024-10-12 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d082922-db3a-33e9-8d85-3bd202aae25c | -9.94008 | -50.06787 | 2024-10-12 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38a57667-6be9-3861-8d22-5436110f4b74 | -9.93976 | -50.06464 | 2024-10-12 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40e16aa2-f325-3fc0-a437-e1a9310f2e2e | -9.83885 | -49.56345 | 2024-10-12 04:06:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f6684f5-6b13-3f83-87db-1f587e03bf90 | -9.83796 | -49.56842 | 2024-10-12 04:06:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b3911362-a58d-30e0-9bf2-2d42dac98739 | -9.8333 | -49.56757 | 2024-10-12 04:06:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d69f00c3-ce92-301b-9fdf-bf71eec2a813 | -9.8324 | -49.57253 | 2024-10-12 04:06:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8601e811-fb7f-3a66-b513-9488d0e51c1b | -4.86092 | -50.77198 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dcd37f-702f-3d5b-89ef-43c913f11aac | -4.83343 | -50.79987 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc9ae121-c71b-38ec-b513-8203e75abbc6 | -4.83324 | -50.80045 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4caed8b7-d60d-3b34-a50a-6699c15b67dc | -4.83281 | -50.80357 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25297146-f348-3aa8-8877-833e97567097 | -4.82856 | -50.7951 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c1d8805-f4f1-30af-bca8-2274a5e7f711 | -4.8284 | -50.7957 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91f2717d-9e0f-3fe3-900a-6fd4f0be903a | -4.82794 | -50.79878 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7983873f-c76d-3d1d-8458-31bce99b49cb | -4.82774 | -50.7994 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3a4e00e-4c6a-37f5-b73c-7a4f0f301119 | -4.82731 | -50.80253 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34ff0ad0-eb7e-322c-bb10-bf28d16d4358 | -4.51798 | -50.42645 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78a072c6-7c1e-3d4b-b946-686715eb8447 | -4.51258 | -50.42553 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce7810d5-edf7-3f9b-a421-78cde4480f11 | -5.0082 | -49.75927 | 2024-10-12 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 266e3f3c-88c9-3eb1-bdc1-b067c059d981 | -5.00308 | -49.75834 | 2024-10-12 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c21d1bc0-620c-3284-8acf-1a5b85067dbc | -4.99793 | -49.75756 | 2024-10-12 04:06:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef4119a5-72d6-38bd-a520-0581731beed1 | -4.60089 | -49.52169 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02d48a9f-c479-3f8a-a5ea-082d481ad5d5 | -4.60039 | -49.52471 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c5ebe92-6935-3081-9282-354e04239b45 | -4.21235 | -49.75301 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61aae405-8368-33ff-b47b-99322b44544c | -4.21183 | -49.75613 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97ebe01f-bb1d-378b-bb35-d732ea001be3 | -4.20716 | -49.75212 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1217ba2e-384b-3b99-818e-792259946131 | -4.20663 | -49.75525 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf25288c-ac4b-32b1-95b3-8e0784dd7280 | -4.16597 | -49.77417 | 2024-10-12 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18affa4a-0240-3a02-b37f-d3d713753c82 | -5.3885 | -50.53626 | 2024-10-12 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a38b029a-4467-3dbc-b1fb-d262f7e326ba | -5.38792 | -50.53965 | 2024-10-12 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b30a9893-2e4e-32cf-bd37-712b35913bae | -5.38315 | -50.53524 | 2024-10-12 04:06:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 285ce5b8-43af-3366-a8b3-0721c92af6ed | -3.56137 | -51.5154 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e4a15449-02e5-3061-8d61-5c83062b0936 | -3.56064 | -51.51966 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 583bb5c2-440f-3193-b9c3-dd8f0e968c27 | -4.65428 | -50.95284 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c73715d-43ab-3507-84af-fe65598034e1 | -4.65366 | -50.9565 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac95e63-0ca9-3eb1-a00e-37d244a2fd5a | -4.02404 | -51.00329 | 2024-10-12 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddeb1624-e10b-3d8d-9eb2-6b98c3223ca4 | -4.02337 | -51.00729 | 2024-10-12 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61a93a18-9c16-3b62-952e-cdcde0f3ed72 | -4.01764 | -51.00673 | 2024-10-12 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e7a69ab-08a5-3f22-967a-f6b8553f111b | -3.78441 | -51.32767 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 70b28792-d49f-3604-b8dc-db4e67696f0e | -3.7801 | -51.31812 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 022c368c-e0b0-3e13-8e22-acc291af0878 | -3.78 | -51.31982 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6d5a58e1-982b-320b-8d96-896d16e0ee75 | -3.77935 | -51.32241 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e0fba2bc-f2fd-3826-a4db-a0207609e93e | -3.77929 | -51.32408 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| ad713763-7e89-332e-84ad-66fc5c75cfb6 | -3.77862 | -51.32662 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 00228d85-035d-3ee6-b037-eb266883207f | -3.7786 | -51.32828 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 19f0e9a0-7f21-3ef7-9d06-e0588d2c5b59 | -3.77723 | -51.33647 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a85dea29-c543-35df-8d35-07708947819e | -3.77719 | -51.33487 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc9875bc-98b7-3e90-91bc-14a0cf6dd1d0 | -3.77361 | -51.32113 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f786538-8590-3b10-bfd2-43f1b139960c | -3.77355 | -51.32275 | 2024-10-12 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9cdf2cf-0574-3e6d-8052-6633dc2a7a1a | -3.48172 | -52.82794 | 2024-10-12 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5c6545e-67f8-3c5a-a5a1-016ce132f4ee | -3.48079 | -52.83339 | 2024-10-12 04:06:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebc4108d-3bd5-3f81-8432-e05f72abd873 | -3.81667 | -52.34258 | 2024-10-12 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README48.md)

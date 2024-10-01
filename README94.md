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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8760417b-49ed-3ddb-a2e9-03e0d3125fee | -22.17971 | -47.52729 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| a2c926c1-4f95-3869-bf7b-7d169e03ba70 | -22.1791 | -47.53106 | 2024-10-01 04:17:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| 314bdc67-0494-3f53-9ae5-f1caac7130fa | -21.5989 | -47.79486 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8ca5e03-6622-3318-b484-08dabf220a60 | -21.59851 | -47.81826 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a3a610a4-e3cf-38e5-9191-a4ceb6cb1f9c | -21.59789 | -47.82209 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5b59f140-6777-38ce-a5f5-ab78ceb15e08 | -21.59726 | -47.8259 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 266a3192-ef96-3481-9394-605d382f2444 | -21.59641 | -47.80998 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05df0c1f-714d-312b-8c67-273484449100 | -21.59617 | -47.79041 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc406375-8c61-368f-ad1d-14e987c9d8dd | -21.59579 | -47.81378 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38278d41-f799-3acc-8942-98f1cc55c194 | -21.59555 | -47.79423 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e4c692b-276b-345a-af56-3194a7407de6 | -21.59516 | -47.8176 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| ae2971f4-5ed2-3101-804e-84584ff3efcb | -21.59493 | -47.79801 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb9dbe2e-fd46-3e2d-8781-6297393e8bd8 | -21.59454 | -47.82143 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| cbe23ddf-f4a5-35d0-9cfa-a46dd1f39bbc | -21.59391 | -47.82525 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 415b9985-9bfe-3aa0-a84a-9706ec1a22a5 | -21.59307 | -47.80934 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 1a3f4b02-4008-3b06-9bd1-2c4409d82462 | -21.59244 | -47.81313 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 44a76dfd-44cc-3573-bdfb-ce3816fa35be | -21.59182 | -47.81695 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 633ec0f4-7963-33cd-8ccc-494604bf1e81 | -21.59119 | -47.82077 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 714aaf25-929e-35e7-bbbc-ea9e3b14af5f | -21.59056 | -47.82459 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8162d1f5-011e-3650-885c-e2b4f5c20f62 | -21.58972 | -47.8087 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| dc3e3abc-1961-3bbb-82e2-b380f4f9bb4b | -21.58948 | -47.78915 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0652fae3-021d-358e-afd2-655396e207f7 | -21.58909 | -47.81248 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4f8dcc83-0f20-3edc-aa99-2dbbbe27c8cd | -21.58847 | -47.8163 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e0bb6172-47ec-3e7e-9881-5fa292b2b693 | -21.58784 | -47.82011 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c8b8c53a-e2d1-3b16-be1a-058f683a4371 | -21.58722 | -47.82393 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| de55fa2e-7344-32b0-8784-62b37a56af3e | -21.58699 | -47.80428 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6f8cbba7-4472-3ec3-84c9-f1419b2578dd | -21.58659 | -47.82774 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 37afbfbe-2e79-37e8-851c-49890356cafa | -21.58637 | -47.80806 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.9 |
| c3640917-3a12-3da6-9492-0c7db8372043 | -21.58612 | -47.78852 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79192e2c-6144-3363-8401-de932f7af48d | -21.58575 | -47.81184 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 385d9528-9d1d-39b7-9a73-4dfc823a9a38 | -21.58512 | -47.81564 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fc525e76-d566-3e3e-ae30-5ea83d292984 | -21.58449 | -47.81946 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 19b35cd7-43fd-3e39-984a-3a036bed54db | -21.58426 | -47.79988 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c95aaa3f-8863-3f7d-966b-f1059c3b03a2 | -21.58387 | -47.82328 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4912832d-146b-3042-82aa-56eb01a8ad51 | -21.58324 | -47.8271 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 324e54a6-1f60-3648-aa2a-b575fe1be001 | -21.58302 | -47.80741 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.9 |
| b1c7f944-25c4-32fd-8d69-82ff0d373ad3 | -21.5824 | -47.8112 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 19404478-0dcd-3bbe-a1bb-17c518680d7b | -21.58216 | -47.79168 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4d5fe248-75ee-3741-a0a4-75ad973d844b | -21.58177 | -47.815 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d421f2c9-2169-35d2-9d79-8a141aae0a8c | -21.58115 | -47.81881 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| dee20922-484b-3e2f-bfb6-9a9420b04da1 | -21.58091 | -47.79923 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 48c643dd-1524-3d4c-a125-6412cadeee79 | -21.58052 | -47.82262 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9efbf1f-0bcb-31c6-8d8d-6bbcea1a2e93 | -21.58029 | -47.80299 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 0225115c-f5d8-3f44-972c-eeb805776925 | -21.57989 | -47.82645 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d60a83e8-cb39-3b98-9f4f-6d8154ca5748 | -21.57967 | -47.80677 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec088c5b-c3f7-3a75-b0e5-84a6631e2802 | -21.57905 | -47.81055 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e88dd3ad-27ac-36a2-a3d6-fb37abf0b2ff | -21.57842 | -47.81435 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a13d0b7-1f44-3bb5-9be3-316f4f877d0a | -21.57818 | -47.79482 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| aec42cb2-1b2a-3e9a-a000-d71014deb924 | -21.5778 | -47.81817 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aaedd6e4-1248-3679-a92b-3cd504e628d6 | -21.57756 | -47.79859 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6d017453-a46a-31c4-ad45-ef6e537d02c9 | -21.57717 | -47.82199 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0715c19-8c46-34d2-a383-27354473dc04 | -21.57694 | -47.80235 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| a0e6cb6b-faab-3e87-ac96-bbe0d3fe5d86 | -21.57654 | -47.82581 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0896e72-ac1d-3260-9048-49deceed9f8d | -21.57632 | -47.80613 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 95164525-694b-332a-ab0e-4e38607668ea | -21.5757 | -47.80992 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b88acc9a-b0f0-3813-8a8f-11c6250e4400 | -21.57546 | -47.79041 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e147fe24-f8fe-370d-b5ee-b0459f42d3bc | -21.57508 | -47.81372 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3759d848-900b-36ab-8f00-1c2a75de1b1c | -21.57484 | -47.79419 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aed08d11-e14d-3ebc-9716-34b61d18134c | -21.57445 | -47.81753 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cadef456-6768-38eb-b323-60a938ea06e1 | -21.57422 | -47.79795 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf092ae8-b79d-3919-896c-c6aabe6ca9f2 | -21.57382 | -47.82136 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca5d198c-8f70-3992-96a6-befdc35c7d31 | -21.5736 | -47.80172 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e352d8a-6db5-35c7-841f-655036743599 | -21.57319 | -47.82518 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa18d324-b292-3b1d-9450-2a26a5b272ea | -21.57298 | -47.80549 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd325130-31e6-3462-b046-dd962eb98af7 | -21.57235 | -47.80928 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 882217bd-ef15-3a95-a819-09b1dc8e98a6 | -21.57211 | -47.78977 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7944a662-4f08-3d0e-9bb2-7969d57d36aa | -21.57173 | -47.81309 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7706f1d1-fd0b-3fad-93ef-ed2c6de5ca82 | -21.57149 | -47.79355 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d3b1b03-d482-321a-bf5d-add33b57c99d | -21.5711 | -47.81691 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c980cf18-ef3a-31f2-8bea-dc4981c51fa9 | -21.57087 | -47.79732 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99ad1df9-f34c-3d76-89e1-5b0e388b2da5 | -21.57047 | -47.82072 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d2fba36-a1ec-3865-bf39-df6e8ec0f5a0 | -21.57025 | -47.80109 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 236e9153-1912-3d84-aac7-2937e0319aaa | -21.56984 | -47.82454 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d51565ab-4430-3ab0-899f-96f1570fddbe | -21.56963 | -47.80486 | 2024-10-01 04:17:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 434fbf61-4de4-374b-8080-3d23d7cdff17 | -22.67713 | -48.34901 | 2024-10-01 04:17:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dc6dd27-5756-3244-a15d-c65fe8fbaaac | -22.58198 | -48.30771 | 2024-10-01 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12eec8ff-5f00-388a-8aad-987c0d494225 | -22.56214 | -47.9362 | 2024-10-01 04:17:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7431f01-2fef-3a65-8e79-c1f3f2f49ba9 | -22.48912 | -48.35831 | 2024-10-01 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65252781-acfb-3d15-a934-e9002b1fb37c | -22.48847 | -48.36222 | 2024-10-01 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b931121-107d-3ff7-9150-8d78bf019aac | -22.48511 | -48.36151 | 2024-10-01 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45b8e319-3359-34a1-95fa-7e2c0f703803 | -22.43891 | -48.40865 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d963c058-568c-3364-9da6-8c98b243ece7 | -22.43553 | -48.40799 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74887b98-aaf8-3991-975d-dd41c79a7c70 | -22.43488 | -48.4119 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94ec1471-97ef-352a-8f1f-cd9f5d1f349f | -23.55005 | -47.6493 | 2024-10-01 04:17:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2f4efb14-ed71-38ab-acb0-f2a11b794513 | -23.98355 | -48.91829 | 2024-10-01 04:17:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59ffdcfb-4af9-317e-9872-41976e5b49a2 | -24.25877 | -48.88877 | 2024-10-01 04:17:00 | NOAA-20 | RIBEIRÃO BRANCO | SÃO PAULO | Brasil | 3543006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 29c21357-49ff-36ff-9527-2b787bfbfa2d | -25.19036 | -49.32674 | 2024-10-01 04:17:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e09080b3-5bda-3ec1-98cc-342b406660c2 | -28.58399 | -49.44133 | 2024-10-01 04:17:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8b205f7a-d076-3675-8668-76f50fb6b2fc | -18.65513 | -49.00099 | 2024-10-01 04:17:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a668b3-6f9b-331e-b310-8f42bf98b6b7 | -18.38523 | -48.22193 | 2024-10-01 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcdc5bec-2f87-3e1a-9d38-49b08393a575 | -18.38108 | -48.22531 | 2024-10-01 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 776441b0-8f5e-3563-84c1-ab652e0973c5 | -18.38041 | -48.22932 | 2024-10-01 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d489529-3c89-3b0d-86ee-ca61404c9c5d | -18.04218 | -48.59605 | 2024-10-01 04:17:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 80614392-b924-3771-8adc-6e00b71f3d1e | -18.04145 | -48.60027 | 2024-10-01 04:17:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 69772847-c80b-30de-8e20-8946115bdf66 | -18.03792 | -48.59957 | 2024-10-01 04:17:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fb13db88-eacb-34fa-8fd7-cd56673a9a51 | -20.8251 | -49.6378 | 2024-10-01 04:17:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 902b6b41-c612-3170-990b-b8b20948d500 | -20.06805 | -48.17516 | 2024-10-01 04:17:00 | NOAA-20 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f045ffc3-35cc-3d39-b099-1dda5289aa3b | -20.06739 | -48.17909 | 2024-10-01 04:17:00 | NOAA-20 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cf6e7fb-f41d-3808-9c5b-b7c4111751b2 | -20.06397 | -48.17842 | 2024-10-01 04:17:00 | NOAA-20 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee5839f6-b2c6-3f8b-8d26-aedd09d88cc8 | -19.69903 | -48.77997 | 2024-10-01 04:17:00 | NOAA-20 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README95.md)

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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77317c6b-b8e5-378d-ba47-66df8488fd95 | -17.04972 | -57.45152 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5ccacc5a-2dbb-3c49-ab36-6d37e44124d3 | -17.04889 | -57.45543 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cccc776a-59d8-3900-8f51-0a2fcf4b34fc | -17.04829 | -57.43071 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c4c4894f-cbaa-3e40-9049-05c9c3eb1df3 | -17.03382 | -57.52618 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fbfe1161-e50f-384d-8c6a-da97ceabc04a | -17.03298 | -57.53014 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 48a0b4f3-c486-341d-9733-b6556bdcc374 | -17.03214 | -57.53411 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5c9976d8-e1fc-3e44-ab29-244ba9b9602f | -17.02737 | -57.52883 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 99e0e024-1936-329e-bb0b-0c1f7d42b079 | -17.02653 | -57.53279 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5879b1e7-e449-3e12-b012-91510a986e48 | -17.02176 | -57.52752 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5a0e2d6f-cd2a-3b51-9784-0c95d0fc4116 | -16.93983 | -57.7127 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9105273d-a77c-34b3-b4fa-94109c6bbc75 | -16.93897 | -57.71679 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04413e7e-20b1-37a7-958b-8b949114e66b | -16.92561 | -57.52768 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 52828e3c-a6aa-3dda-8b02-e35289732e58 | -16.92392 | -57.53561 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 69de9ef8-a4ce-3d2f-a7fa-03c6dbb563fb | -16.91999 | -57.52636 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 06aa52d5-54e0-3f9b-a359-3618dceac829 | -16.9183 | -57.5343 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 77f4b9a8-b71d-3c58-ae10-fb2ea4d9817a | -16.88342 | -57.66962 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e6a27b58-1907-3b12-a64c-e30b2f07b12b | -16.88255 | -57.67368 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 048c4f5e-6a27-3514-9a3d-41b412681dcf | -16.88204 | -57.67063 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 10361aa4-04f7-3033-85d2-bbc312565edd | -16.8812 | -57.67471 | 2024-10-26 04:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ff8f6917-f228-3849-8685-c0f6164b7b65 | -17.7549 | -57.51769 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| cb01c871-02d4-3924-ab50-688b7bcdc2a7 | -17.7541 | -57.52153 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 29234c2b-c5b3-3bf3-be52-c53382d5d20e | -17.75309 | -57.51837 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| 69ea87e0-08d5-3b97-a85f-0ef33639ea04 | -17.75259 | -57.50102 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fa597b4d-2a7f-3725-bdc0-4c0af322a3af | -17.75249 | -57.52919 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1cf00e75-708b-36ef-93bd-a08ec09d2fa2 | -17.75226 | -57.52221 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| d61e62f2-b1f6-3cce-ae7a-106b6fbf31b0 | -17.75179 | -57.50486 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7e98a9ad-619b-3fc0-8fa3-c0e652fd7bad | -17.75169 | -57.53304 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a21fc61f-6177-3c0b-818f-2b719a610d54 | -17.7506 | -57.52987 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b6d33c7b-559c-3903-8b94-d62705078195 | -17.74983 | -57.59758 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8f500155-1986-335a-8bd7-7f1a260d9098 | -17.74977 | -57.5337 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c7a4f73-8941-31f0-86ea-7c6c63b7e093 | -17.74937 | -57.51637 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 032a1fc4-a0fc-39a1-83e3-9649956369bb | -17.74857 | -57.52021 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 4050a4ed-1641-3b3c-96c2-738e6c89f798 | -17.7481 | -57.54139 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 648a5f58-bfd2-3661-b1ee-050f1501055a | -17.74776 | -57.52404 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 9c94b1cd-5edd-3a8d-851b-98edcfb7f750 | -17.74726 | -57.54524 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1c887148-8d38-36b9-9958-8d1f51961b9a | -17.74696 | -57.52789 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d42e650f-cd90-3dd5-b0ac-74ccc2e1ec7c | -17.74663 | -57.60196 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dbc0c9a4-6541-3ef7-920c-b4c05cf08b04 | -17.74643 | -57.54908 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0c75c9bd-fe5f-3ae0-b8a7-1f67e0991c36 | -17.74615 | -57.53173 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 014ec96a-3c4d-34d3-8d73-155fb500dec4 | -17.74559 | -57.55292 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| de13658b-1d8c-3176-8f02-0760125be619 | -17.74535 | -57.53557 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1ac05fe0-f829-384d-99cc-780a8e89cf26 | -17.74476 | -57.55678 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| eb374940-d9a5-32b1-9371-687504d3aa9d | -17.74373 | -57.54328 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5d74d154-79f3-350a-8dd2-43529cd3df0c | -17.74347 | -57.60014 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 83e5c879-7579-37c7-bf2d-fb639b0446fa | -17.74292 | -57.54712 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ed7cb677-7dea-3d26-b386-7310e6c16edf | -17.74212 | -57.55098 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 23a19a02-c211-302b-b815-633342045c68 | -17.74191 | -57.59677 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 416da09f-4055-3310-ba69-5aa3f2061d3d | -17.74131 | -57.55484 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 094d7f22-5483-327b-b62a-c9e66bfd5900 | -17.74108 | -57.60065 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fc3ba34c-42ef-3d45-af8d-2aa8ae9a693c | -17.74062 | -57.53042 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9648451c-dc0a-3b9b-ab1e-f6d8aeddaf77 | -17.74049 | -57.55872 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 52e68526-2da1-3366-9617-7ca9c290503a | -17.73981 | -57.53426 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 06c08f83-60b9-3b03-b33d-53867cdebce8 | -17.73968 | -57.56259 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 240d6362-63ec-379c-9a62-06926fab03c6 | -17.73887 | -57.56645 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 02937584-9826-3501-aee8-2859ad7af295 | -17.73872 | -57.59493 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 477fe23b-297d-36f7-9cc0-94cd5ca95519 | -17.73683 | -57.49325 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7017b12f-b489-3671-a416-b84c77ffa38d | -17.73636 | -57.59546 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1b4f1788-8e76-3d49-9adc-01466e26b4bf | -17.73603 | -57.49707 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| feaf7887-3133-304a-8574-634aca30f039 | -17.73522 | -57.50091 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e060c5b0-f3b2-305f-9662-4f370f079a3c | -17.73495 | -57.5574 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1b14f28a-b2e5-3884-bff6-a0e0826041af | -17.73413 | -57.56127 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c62a7868-23c9-38d0-b502-ed93a9ebac4c | -17.73332 | -57.56514 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3ac5f88d-a89a-3a8e-ac2d-d5b741a28935 | -17.73317 | -57.59361 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0bc43b01-040d-3866-b53f-bd82a1c4069a | -17.73251 | -57.56902 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 78e49e45-eb88-3442-9a6b-5f5d0876e3dd | -17.73235 | -57.59751 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 97618400-595e-3641-b5fc-f564612900e0 | -17.73169 | -57.5729 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b54d65bb-20d2-3a46-9640-f651d8d5b192 | -17.73006 | -57.58063 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 03bf3579-0ae4-3d79-97d9-10d9ec7c8836 | -17.72925 | -57.58451 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 84282c53-f9fc-31c5-801a-6df813cc94b4 | -17.72696 | -57.5677 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c6800dd9-1162-3465-b1c0-8ed592dfbeea | -17.72108 | -57.48552 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 05a6684b-93bd-38ed-bfd7-01a5bec53fac | -17.72026 | -57.48933 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| a488127c-43f1-3da0-81d9-f2be0b82e309 | -17.70288 | -57.48925 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f21bf92d-44e3-342d-a6af-e39ba99538e8 | -17.69818 | -57.48413 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 53db56b1-2433-3176-bd9b-a7b58e4209b0 | -17.69736 | -57.48796 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 828c3131-f446-32c5-8a4e-4f5952486ce7 | -17.69265 | -57.48283 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 65776acc-6df6-3dbb-8c13-14cbc64db8c2 | -17.68795 | -57.4777 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4675bdf5-fa45-3ca0-bb33-cafc7805dac0 | -17.68713 | -57.48152 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 5527f713-7549-38f2-ba9d-11e2c94542df | -17.68631 | -57.48537 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 9eb2adc6-cc69-3525-8a74-dc4b3dc45d4c | -17.6816 | -57.48024 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 33779e3a-ddd7-3b35-9ee6-88e7efcf0c81 | -17.68078 | -57.48407 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 258f9179-2981-3508-9b04-0e0821820a8f | -17.67996 | -57.48789 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3b599606-cd97-3571-adaf-714ab306a049 | -17.67709 | -57.48511 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| df6dbf72-df38-3e31-9264-2aa6034316e2 | -17.67629 | -57.48896 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| d6f788a8-f5dc-3a16-81c3-279f52708548 | -17.67444 | -57.4866 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b7cde2de-4b62-3070-93a9-e69a248f3d61 | -17.67361 | -57.49044 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| f9556f85-564d-3eb1-8f63-9d9702ba32cd | -17.67156 | -57.4838 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 4b3c1af7-8ed0-39fb-8cd3-55be6f696c13 | -17.67076 | -57.48765 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| c982ef4b-12e8-3576-b0a8-bd6bfdceb559 | -17.66891 | -57.4853 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 0f98a961-d690-3296-9f7b-50e4e45e47d5 | -17.66843 | -57.47095 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0f88a8ec-346f-3a21-9805-0b8dea4d9037 | -17.66808 | -57.48914 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5e51a6d4-22ef-316a-aaa2-f7e045deeaf8 | -17.66764 | -57.47478 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a603d1dd-ef6f-3e0e-886d-24196d47c2ec | -17.66604 | -57.48248 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| af70ec54-7ba1-3687-94c9-fb00b6318fed | -17.66524 | -57.48632 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| fe9f398e-fbfc-3915-924a-2cd7aa022bd4 | -17.66339 | -57.484 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 17835ac3-2825-3549-9960-0ba230592687 | -17.88029 | -57.56449 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 824286e9-834c-3734-b32e-ce0fbb28a0b1 | -17.87821 | -57.57412 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fd7b69dc-cb86-3b36-b50b-b22d792ee8ea | -17.87729 | -57.56244 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 518a7225-5f0a-32b1-b49a-dd8090ad4c26 | -17.87663 | -57.56559 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8efb0b19-1299-34fc-b807-6eaccbb7a376 | -17.87567 | -57.51456 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 3de530cb-ffc1-36f5-b03e-d20e5bc8b608 | -17.87494 | -57.5181 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.2 |


[Clique aqui para ver as próximas entradas](README58.md)

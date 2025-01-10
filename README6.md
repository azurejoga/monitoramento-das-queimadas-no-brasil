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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9401cef0-474c-3eb6-b050-c3fa36c72504 | -20.97828 | -49.77162 | 2025-01-10 05:16:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| af3f1d9b-753c-37ab-b0d7-1e1fc8bc1d2e | -29.82954 | -51.88713 | 2025-01-10 05:18:00 | NOAA-21 | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 231d6c1e-54a0-3493-a28e-c9626553da5e | -30.37588 | -56.15894 | 2025-01-10 05:18:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| cf0fb0b3-63ca-374d-b7a0-b42216b3c4e4 | -29.82628 | -51.88654 | 2025-01-10 05:18:00 | NOAA-21 | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| 45d394e3-7dda-3cdb-87e3-69b55eee2fba | -30.3754 | -56.16375 | 2025-01-10 05:18:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 832afc61-56de-3863-bfa1-1d1cd3db16f2 | 4.1609 | -60.68581 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca5e62a0-8c26-3360-8ba5-38ed1029fc86 | 1.17551 | -60.38321 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36416b26-0490-3950-853f-2ab9456024b7 | 1.90559 | -60.67182 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5bfec92-9358-3bf3-a8c3-c612633e1335 | 3.71232 | -60.26315 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c8b2141-81ee-3aba-9838-348532e479b3 | 1.93315 | -60.40609 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4cfb4664-601f-312d-8c55-8298a5895aac | 2.56098 | -60.68657 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 601c1e83-bbd4-3030-9cb7-aa302a6c5741 | 2.57219 | -60.69207 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f04d0289-fe65-3ea4-bccc-036bfb9c9052 | 1.92975 | -60.40661 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 72f34904-12d7-3de9-8723-660242606b79 | 1.34699 | -60.03416 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a0f8db9-272a-3726-aa1f-456e1a5c84a5 | 4.16313 | -60.67829 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 218f4966-fef3-341a-8bb2-cf809a3e16cb | -2.79581 | -54.16815 | 2025-01-10 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0041655e-3a7e-3728-9935-d0907064b49a | 4.40124 | -60.57684 | 2025-01-10 05:33:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c8a4a44-d662-3b43-bcee-3fa4daa6d5ea | 4.15979 | -60.67881 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bacb06e4-44a7-3fa4-b426-20219e8d89f6 | 3.62265 | -60.37931 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53b49b43-4785-3c66-8971-d884a94113fa | 1.3119 | -60.40762 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ccf5eac-dfbe-3f06-9b6f-35e8432bff26 | 2.36502 | -60.15668 | 2025-01-10 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab371ef5-71e6-37a1-8e82-7ecf6f811357 | 4.11421 | -60.85755 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59c6eef7-26cc-3098-a32a-eea0388358b6 | 3.47992 | -60.16268 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 618a55b0-107e-3cab-b66d-c3c383feebf8 | 1.93431 | -60.41336 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3039bc06-3701-301c-89e6-1df3bb2a918e | 1.94325 | -60.86638 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e30733ba-c096-37e7-9fbb-1a20c2400608 | 1.92635 | -60.40714 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 64aa2b84-b15a-321e-9f3f-7f62c10f24c2 | 0.98056 | -60.3867 | 2025-01-10 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de37f13a-d64b-3a49-94ad-de4ff48215c5 | 3.46971 | -60.14207 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84f1020c-87d8-3e79-b847-1fb2a0ff4bef | 0.84242 | -60.59487 | 2025-01-10 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a09fd8cc-3e13-31ee-badd-3f0addf0d3f9 | 1.30565 | -60.41235 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98ff176e-aabf-3a80-9737-c826a4c9f6bb | 1.92751 | -60.4144 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 90dea5b4-7e95-368a-829f-4341b88affb9 | 0.78309 | -60.10273 | 2025-01-10 05:33:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b576920-65ed-3893-8b8c-626000d9ebea | 1.93373 | -60.40972 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b9277efa-2001-3c4f-848e-da7695272c78 | 3.28338 | -61.31879 | 2025-01-10 05:33:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f11d72e8-d968-3a23-9023-3a9fb24bf4ff | 3.70446 | -60.27905 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee4dd227-14c3-370f-a395-8f757aa7546c | 1.38383 | -60.79639 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38669796-d6fd-385d-bf83-4560a38f89fd | 3.70503 | -60.28262 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96f64bdb-fc43-307e-b2a2-dcb3fc59d0ae | 0.78457 | -60.10335 | 2025-01-10 05:33:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b8c05e2-b8b9-386b-bbfd-85d77a27713a | 3.70165 | -60.28315 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a3b95ca-4afd-3cc6-ac8d-99672ca881ac | 1.30848 | -60.40815 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 756c2872-253b-37c4-b2a8-6452846b5453 | 3.32124 | -60.55039 | 2025-01-10 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f718785c-f253-3749-8955-b7ff131ed7b2 | 3.17566 | -60.22483 | 2025-01-10 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1db2387b-ff0e-32ea-9f3e-f2e7fa38d77e | 2.57163 | -60.68852 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31b01225-6910-324d-8955-9b32320f6daa | 4.66128 | -60.16685 | 2025-01-10 05:33:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44b505a6-ab92-316a-85bf-40bcbd500614 | 2.56602 | -60.69667 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30b85858-65d7-312d-ad61-521961411a7d | 3.17509 | -60.22123 | 2025-01-10 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa1a6e79-0b42-32dc-82d0-b49d60cc3e98 | 0.78518 | -60.10715 | 2025-01-10 05:33:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dfa0fa6-7a29-3195-ba0f-30c52007e2a8 | 3.71683 | -60.26976 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceded15f-f9ac-3ea7-8a25-4596d78f5373 | 1.94941 | -60.8618 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9233590d-5ba1-3cfe-9e5d-ee8f956209aa | -2.87529 | -54.17257 | 2025-01-10 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 188b624c-9be3-3df5-b06e-280ddfee0c5e | -2.84828 | -54.00249 | 2025-01-10 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf12607e-cfcd-3243-8031-ed98606a09fe | 3.30891 | -60.53779 | 2025-01-10 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c10e1a55-8c7b-35d8-9365-a63a2c49d389 | 4.13779 | -61.02829 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e22776-6673-35c5-8ddc-e0f79fdcd978 | 0.78368 | -60.10653 | 2025-01-10 05:33:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99fb59f1-c91c-3019-8a15-2ca83312edd5 | 1.80528 | -61.21177 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c84606c-515b-357c-9af0-7c5865ddc99e | 2.67311 | -61.17969 | 2025-01-10 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daeb431d-f75c-3a18-89e7-4c393b8844dc | 1.94661 | -60.86586 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25b05906-b2e7-38fc-b206-54715e1df789 | 3.31451 | -60.52964 | 2025-01-10 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c6217be-1b50-3744-8703-eaf301b970c8 | 4.16035 | -60.68231 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9bd924d-d229-30d8-8d30-d7ab63021444 | 1.94605 | -60.86232 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90c48b36-9591-35d5-9ae0-785d1847a970 | 1.93091 | -60.41388 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 38d4de98-ac41-372f-a77c-ecec25e1fdf1 | -2.85364 | -54.00328 | 2025-01-10 05:33:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd38b315-0cff-3730-b17c-c51222d4dcd7 | 1.34413 | -60.03849 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed8ce1d5-9f80-35fb-a5aa-90f455d7bee1 | 3.1717 | -60.22176 | 2025-01-10 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 444c9d2a-71c1-3325-85be-51b708e3bb99 | 4.14112 | -61.02777 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acdec5e7-5a17-3b31-9d6e-e72887dd766d | 1.93033 | -60.41024 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 34706b05-a4f5-39d8-ba69-6b8532c8df54 | 1.94213 | -60.85929 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6c26237-2345-3135-adfc-f90a9281b305 | 1.30906 | -60.41181 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6095a658-6bc8-3065-9862-7a76cf2e5f71 | 0.97997 | -60.38303 | 2025-01-10 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cc36ca2-4f88-3381-a9c7-3bcccc0ea045 | 3.61087 | -60.39213 | 2025-01-10 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21997601-db8c-3244-af63-429e6bfdd8d1 | 1.94269 | -60.86285 | 2025-01-10 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a1e3078-52e7-3ca2-a76d-dfaa50f2e8fa | 2.4366 | -60.65182 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 142c090e-be04-3fa0-b95d-9fa0ee291cf9 | 4.1367 | -61.02136 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07bd0bcb-21ad-3a24-b98e-29964c665c2f | 4.02476 | -60.61719 | 2025-01-10 05:33:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec78659f-fdf0-3e29-81b6-20f0b4eb1562 | 1.92693 | -60.41077 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 520d8cc9-2a24-3984-8f16-186b0facf5e9 | -2.87579 | -54.16924 | 2025-01-10 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e12f570-097a-36cc-8b82-57236d5a1dcd | 3.30723 | -60.52715 | 2025-01-10 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6980a0d5-ab7b-3a5e-a54b-d0e4aa83a33f | 2.56826 | -60.68904 | 2025-01-10 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554eab5b-5a9c-3186-b7f9-5b50c5092b28 | -6.21562 | -57.77372 | 2025-01-10 05:35:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44a7a989-44a6-3e8e-b6ed-82d53d03e1cd | -3.72604 | -53.77343 | 2025-01-10 05:35:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3eaf0f2-0dc6-3e98-a21d-7dc24f00a979 | -22.60282 | -54.89425 | 2025-01-10 05:40:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1e010810-d31a-3ccb-9b91-b5532fccbad4 | -22.60325 | -54.88844 | 2025-01-10 05:40:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d28f6f04-8ea3-3dcf-86a5-adac50dd9549 | -22.59648 | -54.88781 | 2025-01-10 05:40:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7ae518fe-8f11-34f9-b302-c5c14a919189 | -22.60296 | -54.8884 | 2025-01-10 05:40:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 16ba31da-b950-3616-9cb8-8de6afaaa0e7 | -22.60248 | -54.89421 | 2025-01-10 05:40:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b209c0de-aedc-34f8-8265-91048bca7dad | -22.59677 | -54.88783 | 2025-01-10 05:40:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cc26ea91-8870-32e2-bc12-7d0d69672fec | -21.30191 | -52.06338 | 2025-01-10 05:42:00 | AQUA_M-M | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f0b60aa4-dac1-3188-802e-863ff2addbc1 | -21.30933 | -52.0743 | 2025-01-10 05:42:00 | AQUA_M-M | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1a6138fb-0d7c-3ce5-9790-363e94c76c06 | -20.97711 | -49.77898 | 2025-01-10 05:42:00 | AQUA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 19c9cfcd-b85f-37f6-913d-777ed08ac954 | -22.5942 | -54.88295 | 2025-01-10 05:42:00 | AQUA_M-M | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 2bf1e1ce-4ce6-3e00-b391-387d42a5b536 | -22.60369 | -54.88475 | 2025-01-10 05:42:00 | AQUA_M-M | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 5df16b8a-ed7e-3f17-929a-a0479d2e86e6 | -23.34708 | -48.52642 | 2025-01-10 05:42:00 | AQUA_M-M | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 58c1d3e5-94df-31eb-8214-97e7fd177e94 | -20.97855 | -49.76859 | 2025-01-10 05:42:00 | AQUA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| e911e76b-4dc1-31f5-a858-1a1e5f1940d8 | -21.31075 | -52.06487 | 2025-01-10 05:42:00 | AQUA_M-M | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 40e6b552-7ecd-3855-8446-63ace6f2f6bd | 3.30789 | -60.53096 | 2025-01-10 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75218f9f-159e-3dcf-9a6e-83205b3326ac | 1.34761 | -60.03598 | 2025-01-10 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10f9a467-8199-3373-b21a-ad6278649a61 | 2.56829 | -60.69212 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ed4e701-b2bf-3ba6-b34c-06abc57894ac | 2.57301 | -60.69135 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07e8935d-8993-301f-a4ef-73168b40e776 | 4.15926 | -60.6802 | 2025-01-10 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| effe68a1-72b1-3bfb-8b39-c33336b6010a | 1.94291 | -60.86085 | 2025-01-10 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README7.md)

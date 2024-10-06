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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea8c2596-56ef-3ed9-ae49-6fa5fdcf3c8b | -17.11537 | -57.38379 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1296764f-a5e3-3dc7-bcba-a5843aec4a2c | -17.11501 | -57.3869 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f9f295e5-b7d0-37e7-82c8-c6b7701a877f | -17.1143 | -57.3931 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| af4c8cf4-ba1e-32fa-86ce-4e1c9128d61c | -17.11394 | -57.3962 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8254e2e7-276c-38c1-94fe-97c7805fd266 | -17.11358 | -57.39931 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 606b772b-5793-39c4-8fac-93239ce37eb3 | -17.11323 | -57.40241 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4bcf3b31-f05c-3f75-b121-133612471fd8 | -17.11287 | -57.40551 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 01f44a04-7234-34cf-90f7-c2c7ad1a4f62 | -17.11251 | -57.40859 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| fc67fe0b-aadf-3b45-b160-f5e067541618 | -17.11216 | -57.41168 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8f8a338a-24a7-30f8-96e5-60f68242f692 | -17.1118 | -57.41477 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 55e85c1c-8769-3641-9ecd-0efb086cc73f | -17.11145 | -57.41785 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 25017cf6-5a18-35fd-aafd-28200003ccf1 | -17.11096 | -57.37696 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 236ae1cb-6a10-345b-8120-9b5bc18fe00d | -17.11061 | -57.38006 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| fb17cdb8-5a6d-39a6-b8fd-ad5fe1fd460c | -17.11025 | -57.38316 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| f826a04f-a8fe-3973-8d76-f1d0104d85a1 | -17.1099 | -57.38626 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| de506df7-bf28-314a-858a-29b27dd47c33 | -17.10812 | -57.40176 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 77aa86af-3fb5-387e-9cbe-2e4eb1fb0986 | -17.10776 | -57.40486 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ec3be821-b32f-3ef3-bb59-991e09d33513 | -17.10741 | -57.40794 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 70ea6175-3491-3e4c-8b81-1dde7026c299 | -17.10706 | -57.41103 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 02f0b2ce-132a-3c49-8826-6e23be20eaaa | -17.1067 | -57.4141 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9e9f8ff8-7a33-305d-9a0a-d6159917895d | -17.10635 | -57.41719 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| de4b2e72-81c2-31f4-bb82-e6e5b64a603b | -16.84785 | -57.45899 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 72e29608-b89f-355b-814c-717389deacb4 | -16.83805 | -57.45465 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 05981c31-e419-35e7-a577-41db7a0b9520 | -16.83298 | -57.45401 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a2cad4ab-dfb4-34a5-b007-68acb65a328c | -16.82939 | -57.45344 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 52ad4daf-5610-3c0f-8a2a-61525d1868ac | -16.82885 | -57.45799 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| adc6e0fd-bdf9-3915-ac09-14f5ae2f4df1 | -16.82824 | -57.45033 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 463f95bb-30a1-3fd8-b28f-9f263d6c677b | -16.8279 | -57.45337 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fbc94399-53f1-3e8d-8d32-a7ba0db17be8 | -16.82757 | -57.45641 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 4d53d954-17c6-369e-b509-c5395d8707e6 | -16.82722 | -57.45945 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 26c293d9-7a7e-3b7e-897c-a477cf6920a0 | -16.82432 | -57.4528 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 79e8f66a-9ae1-35e3-be8f-0e0283fe028f | -16.82283 | -57.45273 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ac0ec83b-8bd3-3e78-a5d9-fcf056691228 | -16.82249 | -57.45577 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c670898a-9189-3bc5-a385-7c6a812454e1 | -16.81997 | -57.4461 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f0506680-e5d9-3fc2-b0f6-12e3ee53cf13 | -16.8196 | -57.44914 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| fa1c6a48-3082-3a3e-a98a-a3c90c4617b4 | -16.78618 | -57.47105 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4020405d-9b6c-352a-8cef-37a5c0c6fed5 | -16.77745 | -57.45766 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4ffb406c-d314-3c4b-83fb-c7e80b91c940 | -16.76156 | -57.4618 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b8480eb4-9ce4-36f0-b425-a1464a507748 | -16.71237 | -57.45997 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e915f11f-305f-34d4-9fd6-141a7f30e449 | -16.7072 | -57.44253 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6185691a-eade-3796-89e5-0b670f6091c2 | -16.70225 | -57.4587 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 33d0b603-7cd8-3316-b56e-01618dcc0201 | -16.70154 | -57.46474 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| bc928254-8a53-3f63-a943-383dba8fa438 | -16.69719 | -57.45806 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 13ee58d9-eb4a-310e-848e-059f9dd02c90 | -16.69648 | -57.4641 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| f3cb3cf4-5587-3a59-b246-11ba37da225a | -16.68848 | -57.44468 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2042021d-95fe-306d-b470-76efd9e34298 | -16.68707 | -57.45679 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 9b0ee716-23f1-3635-a45d-68c2dca1e500 | -16.67484 | -57.47359 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 16e863f2-6fb7-3b77-9921-2e29c814f176 | -17.14928 | -56.75038 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b90af38e-b217-3677-a7ef-ad75e0c845a0 | -17.14891 | -56.75381 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 03f3687d-6674-310a-a586-f231a0e5fdbb | -17.14853 | -56.75725 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 90505f2d-9221-30b1-a472-17ba637d841c | -17.14395 | -56.74973 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 8f0734b1-49e7-358d-94cc-ce594a3205a1 | -17.14357 | -56.75317 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fa8ac2c9-b2e5-3c21-a90b-f3fdbefc8d00 | -17.12766 | -56.76559 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 69bf6367-3764-36cf-be26-d6b7a7b88592 | -17.12609 | -56.7649 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c4d43786-6cc4-3189-8f17-a73b9cd3613a | -17.12076 | -56.77862 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a9fd5b52-dbde-37c3-aaf9-16681a81a356 | -17.12076 | -56.76425 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3d40ffed-4265-390e-a401-d8a159badcff | -17.12037 | -56.78202 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 581fffa6-26d6-3572-a1da-846729ad4fd7 | -17.11998 | -56.78542 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1713352b-cb69-32d4-85a1-fdbf928366b7 | -17.11929 | -56.77792 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6748c1bf-bf2e-3ef9-97d2-8141cbb78af8 | -17.11892 | -56.78133 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2c2635ff-8340-362e-abbc-cb2020a7fcc8 | -17.11856 | -56.78473 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e9d9e704-b909-312e-a685-8ec47f878d29 | -17.11818 | -56.75407 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 142bf8b2-abec-385e-aa0e-ec679be8cb11 | -17.11803 | -56.80239 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f5830fc0-eb5e-35bc-93b5-43921047bc83 | -17.11779 | -56.75749 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 73e7b045-96e5-3b64-b56b-85f458fb26ae | -17.11764 | -56.80577 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5f55b12c-8062-3ecc-883b-902ee926d3bf | -17.1174 | -56.76091 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| eec1039d-e57e-3929-8e2b-3ac61129add0 | -17.117 | -56.76432 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 72e487ad-9f66-3031-9d48-e1b86490c03c | -17.1169 | -56.74991 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5a06db92-19fc-3f2b-b95c-2d6e9f574f05 | -17.11673 | -56.80172 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fef09afe-4d88-30ac-97da-c912f431b534 | -17.11661 | -56.76775 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e1d44f39-8df5-3f38-8bd1-2291ffe444b6 | -17.11653 | -56.75333 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f5040472-208a-3d42-9749-1054fb56ada8 | -17.11636 | -56.80511 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 19de733c-eba1-3f88-a9e3-c9f84d9a57b4 | -17.11616 | -56.75676 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fbd8d07b-d63b-3ba2-ab84-93592dad6842 | -17.116 | -56.80851 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5467b9e9-f1d0-3863-b36c-0cdfa95c0f83 | -17.1158 | -56.76018 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e932b3f1-880b-3f1e-b85b-3fb31c070534 | -17.11543 | -56.7636 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aabe80f6-65dd-3668-8264-5e302db3948d | -17.11506 | -56.76703 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b3668e6f-1650-37ee-b142-09df50d4e436 | -17.11402 | -56.74318 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1f7f0361-a25e-3d0a-b046-c88c3a07b4a5 | -17.11362 | -56.7466 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6e5cc4da-5143-36e6-9761-1986017fe905 | -17.11271 | -56.80175 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9c470186-9780-33c6-a24c-f3511482c3b8 | -17.11232 | -56.80513 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| cb2314ec-6881-3ed4-b545-285d868984b5 | -17.11229 | -56.74239 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f36211ae-592d-3f46-94d4-72c91ab44ddd | -17.11206 | -56.76028 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 91c0913f-76e0-3634-b970-741b712fb603 | -17.11193 | -56.80852 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 503b9905-c04a-39f1-84fe-fc4887158e40 | -17.11193 | -56.74583 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 52178584-6e06-3953-b0b3-5eb255dcbf02 | -17.11177 | -56.79769 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 880f7d5f-2b8e-3722-9ca8-f4c57707365f | -17.11167 | -56.76369 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9aac7ec3-827c-3314-816f-4b714aa9eabb | -17.11141 | -56.80107 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b03afd8-f970-310e-be32-afb1138fd14f | -17.11128 | -56.7671 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 32987405-27cb-3d8a-aae4-6f34667544e3 | -17.11105 | -56.80446 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| af2cb27d-cb2b-3f05-8be6-a3bd49cbf064 | -17.11068 | -56.80785 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2cd1e636-8e3d-3d82-9eaf-e1ffa76b0c35 | -17.11032 | -56.81124 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6d57bece-f04d-3e90-817d-9ec37f483ba0 | -17.10778 | -56.79775 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 83c73019-b6af-312e-a095-882caf2ec2cb | -17.10739 | -56.80113 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 78e31c64-937a-3b9a-8935-9476162ecaea | -17.10701 | -56.8045 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a8b1135f-0497-3d76-891f-9e9a33e835a6 | -17.10662 | -56.80788 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6f0d84e5-6f86-3804-a52f-f45e94058290 | -17.10645 | -56.79705 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3bb867ac-de13-3374-b6a9-f5dafbed395b | -17.10609 | -56.80044 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 56553832-118f-3bc9-a009-b8c70a3bfef3 | -17.10573 | -56.80382 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 34399189-5127-3b56-a72e-fca2235e7d39 | -17.10537 | -56.8072 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |


[Clique aqui para ver as próximas entradas](README146.md)

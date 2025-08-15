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
| 671c4250-997f-3fb0-a153-3a742d1529d3 | -7.14491 | -59.6306 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af172cc7-d7c1-3423-8177-7f5a1cbd52c2 | -7.30592 | -60.62589 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9209af8-0d6c-34bc-b39c-88869b12c596 | -7.07841 | -59.2105 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdab5b00-ad60-3496-b25b-5bc2b6eb3af0 | -6.92865 | -59.54012 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d1373f1-3fa5-32c2-954e-c28c2a1e94ff | -6.67334 | -59.08782 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be91d335-e769-3183-9a66-6d292f42719c | -6.87471 | -59.15716 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbcb9010-3416-37af-850b-2df2b07402f9 | -6.90757 | -59.14853 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a13510-6de6-3090-b2a2-76fbc08c0547 | -5.80428 | -59.22178 | 2025-08-15 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f5791ff-4b8c-3a52-91ab-fa0ae362543b | -5.73292 | -59.88702 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dd2376b-fe47-3e23-adc4-b858f2cceae5 | -6.78928 | -58.79048 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16d615d7-5919-30a1-9840-d2ad17a11918 | -7.14144 | -59.655 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ce821f-7554-3acb-b875-cc8c198779e2 | -6.92209 | -59.14191 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0025af44-576f-3a30-92da-cffc322aa630 | -5.92183 | -59.92961 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3b8ece7-1eb6-3d6e-ad10-3c07f4759356 | -6.64616 | -59.08806 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f184173-e3c4-372b-8616-d16d54d88bd8 | -6.90682 | -59.63242 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0380ba78-0213-3632-a8c2-b83750ca40ad | -6.90694 | -59.15288 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 566a1273-2a73-3508-8dec-123c11ab27ed | -6.88223 | -59.13588 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dca2746d-5e85-3fb4-9ee2-d171ea445e64 | -6.71105 | -58.82058 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 817250e1-cdf5-34d2-9b4a-ff031dbebb0c | -7.01319 | -59.82695 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ab5f8c5-3afe-3a17-8eb0-d6791e7dbd05 | -5.45039 | -60.13723 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1715b7b0-4cd7-30bb-b1e2-bfd0cc39a5c0 | -7.15236 | -59.63993 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1041adba-9863-30e8-bc22-dd7f0d4e48d4 | -6.48715 | -62.93444 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c5857359-d417-3275-bbee-c33d280c26ed | -6.47954 | -62.93727 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5e02c2c-7d96-37a3-b375-ed26d63e43ec | -6.076 | -59.9627 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ee6241b-63bc-3d3d-8afa-d38fe260cdf0 | -7.09087 | -60.03928 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa1c81b3-72af-38ed-8d3b-a94258a090c5 | -5.75302 | -59.89412 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f1f2cd7-05ee-3dd8-a36c-a0f814e8cb59 | -7.30996 | -60.62647 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cfc84db-7712-3bc7-a8e3-789ba54688fe | -5.44634 | -60.13662 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3278adf2-b11a-3334-8d7a-96c10127722c | -6.89675 | -59.12917 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b5c08db-1a98-3034-a466-8f28984374c3 | -6.66976 | -58.81921 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a1bbcfc4-ada5-3f66-b163-2762864b5034 | -6.79118 | -58.78756 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79eb4e91-ad6f-348e-94bf-d0e19ff82ee7 | -7.09166 | -59.21253 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e31475f0-8266-33bf-b42c-ce765e9d0565 | -6.88542 | -59.14529 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a592866c-97d9-356f-b8e2-de137d752139 | -5.4585 | -60.13845 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 206ecb40-2658-38c3-80cb-f16730881aa8 | -6.67397 | -59.08334 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbaed074-1029-3cd7-8142-f2b80d559d6e | -7.0854 | -59.22497 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56753b66-d877-3a7f-8f26-e60f76a72a79 | -6.99928 | -59.98365 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2b7888f-1ab9-3036-b60d-dc02a64ac36a | -6.69818 | -58.84663 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a78c9c16-6458-3e74-ab8d-4543c85f0c40 | -6.70653 | -58.81992 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 057dbabc-0e1e-3e47-bf7a-2b6fb6dd8f97 | -7.24859 | -57.67341 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7ac1ee8-095a-3334-87c9-f11f31f03f05 | -6.87913 | -59.15781 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd2262fe-2386-3080-aa9f-98cce4b929ee | -6.88417 | -59.15411 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab78f160-289b-35ae-a85c-b108bff0c094 | -6.88356 | -59.15846 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b41ae7bf-4768-3b17-949c-ba074ed8c6ca | -6.88398 | -59.88506 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5731c173-77d1-3266-bb10-4ffb8bf5ca4a | -7.1316 | -60.12277 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53e3c54a-d288-3372-be54-bd096a893c75 | -7.29381 | -60.62412 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fcd14c3-909f-34ae-a915-58b0b196d880 | -5.45497 | -60.13426 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 402a34b4-b635-34c8-8794-814d7fc9b4db | -5.92542 | -59.93399 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a2afe8d-9751-396f-994a-9fd84c2c952b | -7.1257 | -60.12206 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d656af2b-a4fa-3e93-826f-04b24e09282a | -6.72781 | -58.83245 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 731447ad-26d4-30fb-aaf5-c3bdad151b21 | -7.31045 | -60.623 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73afb52c-e470-3624-9282-fd30fe6f48a5 | -7.26301 | -60.63092 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a836beee-708b-31e3-ad65-8cc62866a094 | -7.09486 | -59.22189 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be9535e0-ba6b-3dbc-96aa-0ebabc375ab6 | -7.08725 | -59.21183 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb3cab7e-e28f-378d-a3b0-1bdac23955a4 | -5.4615 | -60.14622 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a9292b7-7e28-33c8-888c-a54e9c513037 | -6.89047 | -59.14154 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15203ff4-62b4-34dc-bc8a-bf6374c87d8c | -7.08664 | -59.21619 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd62ceaa-f6c1-37cd-9116-82bdd2651f6a | -7.28928 | -60.62701 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c98b981-d956-3a3a-8ae1-622c29a45847 | -6.67758 | -58.81736 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84e744c1-2ead-39eb-8162-b1869e4ddee3 | -7.24211 | -57.68367 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18c48c0d-57bd-32df-8da7-52c2600d767b | -5.45092 | -60.13365 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9699f342-24a0-31ef-972e-f22d9025ea24 | -5.45392 | -60.14142 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f9bbea80-944c-3299-b4a1-f182282062c9 | -7.24518 | -57.6619 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53e8910d-669b-3522-a251-bf246fb18330 | -5.7423 | -59.88086 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c08ae4c-db65-3b40-9bd6-fbda57006000 | -6.91704 | -59.14557 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4be8698-f3db-3ac7-adc0-e98bc8b2f827 | -7.08037 | -59.22869 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cff7135-b39a-3285-804f-7d6bbfa721ef | -6.93295 | -59.54081 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 0f320042-8830-3672-95c5-1a81a3c7f32b | -5.4555 | -60.13067 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06200b70-5805-3af1-a983-563bf78e2b65 | -6.87375 | -59.83583 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c62feb7-a740-3577-8cff-24ca4635013a | -6.66461 | -58.82314 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd60dac4-4996-3152-9655-c047427c9e1a | -6.94724 | -60.13885 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c174357-4501-3125-aa1d-68001bb41fb3 | -6.90251 | -59.15225 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9c5802d-5e7e-32c1-b354-f26125125b84 | -6.87799 | -59.83638 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be195750-679f-3864-a313-cf411179ad08 | -6.87431 | -59.83192 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c92000a-0e9f-37f7-b45d-1effb8de6f95 | -5.46009 | -60.12768 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70652c70-1d05-3268-8d3d-d21e493387e8 | -7.09105 | -59.21687 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d164c11d-6bd6-3a08-96d1-01a1f57fe869 | -6.70008 | -58.83309 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0770e243-3e58-3305-8c88-c25bbe8bb40e | -6.92434 | -59.53945 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 887bbb37-9e47-377a-bf54-734ab6e7ce18 | -6.88666 | -59.13652 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8afebb2-d721-38f2-86da-44d644cdf911 | -6.78665 | -58.78685 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44ee2bd7-0a12-3278-b6f6-cbae725d7815 | -7.31399 | -60.62708 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f93cb13-1d35-3b94-a9dc-789e00d6a38e | -6.99872 | -59.98754 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7563537b-e30a-354a-a78a-a9ad11e2bc1d | -6.91262 | -59.14486 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57f64234-38f2-36ab-8cd8-d5b33518879e | -7.09547 | -59.21756 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb9e9fa3-176d-374c-a266-940dd1d3b20d | -6.89232 | -59.12849 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42a50a9d-8ed0-3ff0-8717-2ee23d4d1979 | -6.72008 | -58.82191 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 130a44de-6095-3c0e-9269-0124fe707a79 | -6.8732 | -59.83973 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d789e1f9-0cde-31b6-9feb-910503136ce0 | -6.92146 | -59.14627 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb3ab3a4-2cf9-3c2d-bac8-3eeec9bb061a | -7.43359 | -60.02835 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ec9310b-0b79-3b15-a164-fc60e80a9ef4 | -6.8882 | -59.88564 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06e0387e-5ae6-3cc4-84b0-022aa6c04af1 | -7.39797 | -60.00709 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af94b03c-0980-31fb-a6de-944e440a10d3 | -6.07185 | -59.96218 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03f1fab3-138b-3746-82af-eb36438eea3d | -6.64983 | -58.81795 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ea42aa0-8d5a-350d-a4bb-90d5b4638e8f | -6.91387 | -59.13613 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43dd7b9e-044e-3d56-85bc-4917fb6eda2d | -5.93839 | -59.93208 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffa4cf01-7971-3557-882e-01ae33f8b70e | -6.94392 | -59.52567 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f437f2-d15b-3b7f-9e4c-0ebed4245495 | -6.69944 | -58.83762 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4bb617d0-fe2e-33b3-9c0f-e8149850df8f | -7.12338 | -59.62761 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb0523e1-59cf-3aae-aeff-e577fdef4244 | -7.26251 | -60.63437 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c157aab-60e4-3572-89fe-31dd525f0e91 | -6.92084 | -59.15057 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README58.md)

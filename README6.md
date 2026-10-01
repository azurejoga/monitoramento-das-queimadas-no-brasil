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
| 62a5a029-6ab3-3d13-94c4-cce25c2b6dbe | -4.25124 | -50.76768 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 1d8d7d7c-2e20-3cbd-aeff-1ad0f71efab0 | -1.44952 | -54.46483 | 2026-10-01 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4fede442-c4ad-30fd-a2d4-d4dceab8b1d7 | -5.85129 | -57.7624 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 79b64fc8-3b4f-3b2b-9459-78bd4f7f31f7 | -4.86621 | -45.85701 | 2026-10-01 00:20:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 5ed2d4d9-7a60-3259-8a76-7f0f2a1a4c3b | -3.14634 | -53.74474 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| da06bb87-4bf6-33b0-b351-3768309e63de | -3.49292 | -54.72482 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 45ff35f4-bfe2-385a-b9a2-e9c587781098 | -4.24753 | -50.74234 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 18b49e67-bc4f-30ea-8222-4cfc63ca2da0 | -5.7688 | -45.16978 | 2026-10-01 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 87492ead-b5ec-37ee-8524-c536b9b01356 | -3.02732 | -51.2771 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| f76cf3a8-5b95-3784-8ae4-93748f69b820 | -4.30531 | -50.77285 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 76cf611b-0b32-3c53-b46b-ee28dab53cef | -7.68329 | -54.76984 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 509506d1-f741-3a45-be88-1afdb12d5adc | -4.29305 | -50.76168 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 367c157b-50a4-36a3-9948-01b7108fbe62 | -4.29667 | -50.78701 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 66fddd20-dae1-38ad-a1be-305e51f51348 | -4.258 | -50.74086 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| a30bfeb1-c91d-3a9a-8e7c-0d6090ffaa4d | -3.4235 | -54.54667 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c71dbb93-3092-3b78-aff3-f5cacb65dd54 | -3.17832 | -60.05413 | 2026-10-01 00:20:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bd7b7b6c-abfc-3e8f-a012-828f0f8c1e99 | -3.1846 | -57.84058 | 2026-10-01 00:20:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7099cbc6-d1d3-3194-8d45-4fe4425c60b9 | -7.33557 | -54.99009 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9875ef0e-bf03-3988-949e-77edeac68a2c | -3.09976 | -50.29632 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6fa26f4f-90a1-3714-8de3-e08e2f5b59b8 | -3.48689 | -54.68097 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c1b1bb92-acd5-372d-bd7c-b3c96f62559e | -1.64274 | -55.13168 | 2026-10-01 00:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6969b1c0-4d1f-3b11-bf4d-87d3fcfd2f99 | -7.49386 | -55.00796 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 713164bb-83f3-3e70-90ee-483422c30f2f | -6.43203 | -55.80432 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1de45b0e-81ea-3d03-9f89-c5cc183e178c | -1.08497 | -54.10021 | 2026-10-01 00:20:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b46a8c25-920a-38fa-8d16-c9ba1a3da4b0 | -1.63393 | -55.13291 | 2026-10-01 00:20:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a5f2ca37-e4e9-3e42-8e54-66cc2e2d5a42 | -3.97704 | -51.91797 | 2026-10-01 00:20:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d089cfe6-42ba-3e63-9c8c-35c8ddea9a91 | -3.58625 | -53.9979 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6f2b96f3-6fe8-3fff-ac32-4a7197107bb9 | -3.00775 | -53.87796 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| dabf2dc5-ced8-31f1-82ef-de38c9d8c5c8 | -7.49757 | -55.03524 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4e112751-e402-3232-8c00-04e75a5245bf | -5.86143 | -57.76101 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 74eba3e6-9927-3771-acc6-ebb5f4f5ef5e | -6.13842 | -53.25772 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| eb1a0f15-3bd6-3773-807a-605bc1f1a10c | -6.5465 | -55.28411 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 1adc7879-83b7-342d-b72b-2077e4c5de1d | -7.34224 | -55.58915 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e5db60f-0996-392f-a212-f4dff255a85d | -6.03341 | -53.36184 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d2b42aba-75d6-30e5-92fb-b8570ce59fe4 | -7.45687 | -55.00378 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cf159281-be3b-350a-beac-9cd3dd880f81 | -2.9721 | -51.03189 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 4529f7a0-d917-3253-a487-eb41c3d4ff6d | -5.12484 | -56.00854 | 2026-10-01 00:20:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| f51b2033-1361-3023-b356-21d8e1d6b628 | -5.92463 | -53.50219 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 65388474-f06b-313c-812c-822671e15ed5 | -3.02434 | -51.27116 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bc2317dd-1963-3b98-9dee-0582fcb410a9 | -6.14967 | -52.74329 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 505f6450-6815-338b-a32c-1cca06d5cd48 | 1.12276 | -50.74535 | 2026-10-01 00:20:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 33d3d88a-abcd-3a0c-8187-b0dd012ca696 | -2.95429 | -54.09282 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8c4850b3-2a7e-3c3c-975d-6200845134df | -6.66505 | -55.07661 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 16e0934f-5089-360b-9442-08be3af368cf | -6.74409 | -55.58981 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 076caa54-dfb7-33a5-8e22-6738ea24aabd | -4.25987 | -50.75367 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 465.7 |
| b3955ad3-8400-3925-b600-7b6c896ef59c | -3.16453 | -54.07244 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 91ae8a7a-743e-3427-b141-511a4f5ac5e7 | -6.23591 | -47.44602 | 2026-10-01 00:20:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 42d5e9bf-f81a-3bb8-9c59-7b87bd69c41d | 1.87242 | -55.64463 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1b1f1361-9bed-3094-a7fb-26b29186bbf6 | -3.13738 | -53.746 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b6ef1aa6-eacb-3071-ad64-eef7d3c7d2bd | -5.97011 | -53.56883 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 56828457-bc5b-37e5-aea2-35da96750655 | -5.29908 | -55.86746 | 2026-10-01 00:20:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b7ac9a8f-e1a5-341c-8f7d-84725c9f6e95 | -6.14734 | -53.25645 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b08654c2-af4c-31bd-bb24-114fadc68ca5 | -6.88999 | -52.50409 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 792077c4-3b73-305a-a483-b93392fb57b7 | -7.33435 | -54.98101 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 80ab48a7-4da7-3dde-9b41-d395640a2f30 | -2.90717 | -54.14491 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 87f5cd73-c752-3a2c-819d-4b163eec3362 | -7.71764 | -54.75587 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| daffc75c-8192-3250-bac1-6dad75dbd238 | -3.8008 | -51.03566 | 2026-10-01 00:20:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 4a27eb97-4a73-3655-94f8-5d14a15ae6ab | -7.35135 | -55.58792 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e3a20085-868d-3315-b60a-1b4b012ffe5a | -6.51163 | -55.36994 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2ee90c24-829c-3558-80d1-55a7cb891e8f | -6.74819 | -55.07705 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a6228cd-f0ca-348d-a081-4d7c453a6444 | -3.16578 | -54.08138 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 484.5 |
| d35d70e3-fd7f-3293-8765-54cdaeb7cc5d | -6.00652 | -49.56867 | 2026-10-01 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ff1a95b4-8a03-365a-ae17-5d543fef2267 | -2.9222 | -54.18817 | 2026-10-01 00:20:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 289d65df-7b56-343a-ac90-0794f4406a7e | -6.11443 | -55.69984 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ea6d9318-beb5-3eba-bfff-19e9e2d74e74 | -3.96435 | -48.13847 | 2026-10-01 00:20:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ab7defaa-4439-3476-8446-9bddcea3de83 | -3.72358 | -59.41479 | 2026-10-01 00:20:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f2edc75b-23d4-3337-980d-b25e547244a7 | -3.15566 | -54.07369 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d5ed3f77-6a7c-3f9e-8a6b-a817293a602f | -5.11574 | -56.00971 | 2026-10-01 00:20:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 137a1a0b-726b-364e-ada3-cdc840358165 | -2.55242 | -57.85767 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| fa28dc20-cc18-346e-ab6f-f48d58365ada | -5.85307 | -57.76775 | 2026-10-01 00:20:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fe49e737-6b5e-3d7e-b84a-170c4c3ee0f0 | -4.63939 | -50.60887 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f005ec3f-12ff-3211-8963-70bf376a10c9 | -6.73502 | -55.59105 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 790260e7-38ab-38ac-ba1e-483f0faa41f5 | -4.26849 | -50.73941 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e327623d-f175-30bd-b8c0-49026a318d25 | -4.31932 | -50.79662 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c91cdbad-31c1-3b3b-b4a4-84b7e2479f91 | -3.14508 | -53.73565 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d7295c19-85b6-3417-81f4-0c049d94f691 | -5.30036 | -55.87681 | 2026-10-01 00:20:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2ddd9736-c508-35f3-8c71-487782b89c75 | -3.26134 | -52.58427 | 2026-10-01 00:20:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| d270cdc7-8395-3c12-80ac-b982a2cb9620 | -7.07924 | -55.48114 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0f468054-560a-3aef-a0ff-a01345f72c88 | -6.92647 | -59.27171 | 2026-10-01 00:20:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a43f354e-8caf-3f9b-b6f2-7332355d6546 | -3.42229 | -54.53789 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1a4603e6-df3f-3ad4-a878-49560aa503c8 | -6.02451 | -53.36309 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9652d494-64da-3462-894d-1ab969d5a7f0 | -4.27031 | -50.75204 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 213.4 |
| 85bb0315-1ccd-3427-9161-41e3a52a672c | -5.86931 | -53.50727 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d0268356-893f-38cf-8840-26052898f000 | -3.00054 | -51.03432 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8f0253c8-2745-31e7-8990-aece756a4797 | -7.46458 | -54.9935 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 218b6214-059f-3baa-8e75-47658f8ccd8d | -5.73712 | -45.17545 | 2026-10-01 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| e1acde42-f283-3208-8d2b-dea53c1d3c74 | -2.89975 | -54.09136 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 7beef95a-e511-3aa1-ac01-01764574c8b4 | -6.13851 | -53.05651 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad34ee2e-5c22-32fd-91c8-266b3cd7d207 | -4.03521 | -54.23864 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6390559a-e796-32eb-bb8d-559326cd55c2 | -3.10181 | -50.31051 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| cdcc053a-d464-31a7-bed9-1db1561c826e | -3.56785 | -51.48935 | 2026-10-01 00:20:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 261.5 |
| 714d0fa4-0b4b-3e05-8186-7c81ad40b9ce | -7.49262 | -54.99886 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5095f166-5fe8-3b87-8479-03ca5067d4c1 | 1.70035 | -55.90014 | 2026-10-01 00:20:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d11b538c-a0c9-3ded-bf8d-2d23a78748ad | -5.12362 | -48.79524 | 2026-10-01 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e1f0845d-dc77-30b2-b66c-8a804c8ba9d9 | -6.13968 | -53.26682 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 717819fe-40ba-34e3-a874-ded4f403e1ce | -6.08985 | -56.47744 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bbe59b97-e60c-3ab1-bbc8-7b2ebbb9b59a | -2.14973 | -58.11622 | 2026-10-01 00:20:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c29a07d0-ef1c-39cc-ba58-cbe1e6d1c74f | -3.23434 | -54.31604 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 599fe8ea-862f-3e3a-9f8b-7d9911a8b3ed | -7.73145 | -54.79072 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eb54480f-c04d-3f0e-b13b-b3f3efcb6ec3 | -3.59995 | -54.55458 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |


[Clique aqui para ver as próximas entradas](README7.md)

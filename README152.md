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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7615ba57-840a-32fb-9d41-b1cfea72f18e | -16.76754 | -57.41437 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 62e37094-7b27-3a99-b917-5638f8cb8e2d | -16.76752 | -57.38998 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b5f34a9b-ac12-3b47-872e-770c4e515d26 | -16.76638 | -57.42229 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5795140e-251d-3a79-8243-1b9af2443180 | -16.73276 | -57.43321 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 4c7ec6bd-d4c6-3e0e-aab4-85d580640151 | -16.72695 | -57.42419 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d7d8ce56-1a43-3b14-98dc-cd3a7557dfc5 | -16.7258 | -57.43212 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 96fca3ca-22f3-3645-97c1-192ff59239f6 | -16.72347 | -57.42364 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 0b141ad1-5804-3d35-9686-edfccfb28bb2 | -16.72323 | -57.41591 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ae30ef90-664f-30ec-92be-03b7e7d4a26a | -16.72289 | -57.4276 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 01632dca-2f5a-3af5-aceb-c1e4054b1837 | -16.72206 | -57.42382 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 7c254ec8-18ed-3fbd-ab4c-877188dbb32b | -16.72147 | -57.42778 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e880dce6-54be-3913-9d14-9546d14f78f0 | -16.72066 | -57.46772 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a2204251-3c53-3c74-bce0-184c60e06f75 | -16.71561 | -57.46728 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6352a852-0d44-3d20-b1b8-705847b269a1 | -16.69892 | -57.33892 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9cd63222-19f1-367d-9509-7dbcde1cca2d | -16.69766 | -57.46849 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c5b48775-6c26-3804-9d7b-3b36082aaa52 | -16.69543 | -57.33838 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 08c23442-d50b-3f78-8fc8-34842ebafbd0 | -16.69194 | -57.33783 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a3d293e8-6c18-3c23-a732-deb1f2b23338 | -16.69077 | -57.3458 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9f93f512-daaa-3736-97ff-5bf4474a5ca2 | -16.6867 | -57.34923 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ab10c656-3a1c-31f1-b403-ea3dcb82f78c | -16.68612 | -57.35321 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 88b35dea-911c-3d7e-967a-e4a7ff3ab30f | -16.68554 | -57.38158 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e830eb13-f6a1-36f2-b18e-03465321bea1 | -16.68496 | -57.36116 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d5c2233e-05f5-3b82-ada9-5d1897bb2ce0 | -16.6838 | -57.36911 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 4206d8d7-f595-3af1-ac03-67acdc1b7d8b | -16.67045 | -57.46016 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a6298eea-49a0-38de-a973-2ebd2eb381c1 | -16.66698 | -57.45961 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 260999ff-03f2-3ddf-8811-21db49a66010 | -16.65473 | -57.34828 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b5d49a9e-5c13-344d-b0b9-6f6dcf92daf6 | -16.65413 | -57.32781 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4bb82d5f-3c21-3f8c-a028-87e28e200254 | -16.65125 | -57.34773 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 815ec87c-e5e2-3b4e-aec1-353a01941d0d | -16.64369 | -57.35061 | 2024-10-02 05:12:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4e97f51c-eaa3-3f5b-ad9d-0d6288a78b76 | -16.88168 | -57.68462 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 06950b6e-4ac0-3900-a9b6-8618d9c3d513 | -16.8811 | -57.68851 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| b6f19c46-8e70-34a3-9fc8-f46baba7c321 | -16.88052 | -57.69241 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2aeeb099-48b6-325a-bd2a-63295fe35a31 | -16.87994 | -57.6963 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8c14c4a3-639c-3df7-b509-c55439d57618 | -16.87936 | -57.70019 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e947ce5e-a59d-326d-b6c1-96855cf556eb | -16.87765 | -57.68797 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c18b7eea-822d-339a-ab8b-b06cd7247ee9 | -16.87649 | -57.69575 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 676a522b-258f-363a-b5b5-c1ffa5e61b56 | -16.87592 | -57.69964 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 29b3db8d-96bd-36ed-949a-b040d5d5acfd | -16.87477 | -57.68352 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a7b27dce-1bb7-3c67-8dea-9e745968fc57 | -16.8742 | -57.68742 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e0e2c56f-ba4a-329f-95f3-fcdc0ad933a4 | -16.87304 | -57.6952 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0f6f5f9a-92a8-3a13-8eba-46d838a05fc1 | -16.87247 | -57.6991 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 647dd835-c743-34de-93d3-fe8a1b4d982f | -16.87074 | -57.68687 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ee23cbb4-6fa5-3ce8-b69e-c592d3469c05 | -16.86959 | -57.69466 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6cc58b7e-abb1-3c03-9c98-bff3c02a6e35 | -16.86901 | -57.69855 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f2cebfa1-058d-30cb-bdf6-83a5ac2ace62 | -16.86323 | -57.78498 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 37435a07-031d-3401-9d75-5d3dc5c55f81 | -16.85865 | -57.76841 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 49ca14f5-8422-3870-a019-911113893bea | -16.85636 | -57.76012 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8110a7f8-3b21-3875-9782-2c27d3d93355 | -16.85578 | -57.764 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 59688b0b-5a04-3da5-9f61-6262f6212369 | -16.85234 | -57.76344 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e95fa837-825a-395a-a58b-ccd020615e75 | -16.84947 | -57.75902 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c759fec0-cfb4-39b1-a059-b53e5d64455c | -16.8489 | -57.7629 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0b075730-bd39-3e15-a171-e5f234b3b556 | -16.84718 | -57.75072 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5ea12c1e-9bf7-307b-8f57-ec2104ef6f95 | -16.8466 | -57.7546 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c57c17ba-2ad8-383f-9ef8-591dc6161c6c | -16.84603 | -57.75848 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2d12e3fb-4912-3223-885a-6ccf8e8d3c9e | -16.84546 | -57.76235 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 70917afd-18b4-371c-affb-41a4f8e950a0 | -16.84488 | -57.76622 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 27a7c44d-76b7-360f-944b-3981f8de93b6 | -16.84487 | -57.69471 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 100bdbf7-5172-3d60-9572-a828a310bd00 | -16.84429 | -57.6986 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0dd9ec7e-c54b-3093-9367-9d62796fa806 | -16.84316 | -57.75406 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| aeae0dfe-4d1d-34b4-b867-3eb1ba5fdc83 | -16.84259 | -57.75793 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bef490d6-9884-3a0a-add5-0580ba663982 | -16.84144 | -57.76567 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6ff91a11-07bc-3246-ae4a-79ff73b0444d | -16.84087 | -57.76955 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5af0af98-51ad-3cc5-b000-ddd85758ba3e | -16.83915 | -57.75739 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| eeaf1544-0e63-34fd-beb5-0cfd587ca68e | -16.838 | -57.76512 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1af40d82-aa8d-399c-b606-e098ea288d7a | -16.83628 | -57.75296 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| eca59cfc-ab2e-353e-911c-5af4e0cd3523 | -16.8357 | -57.75684 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5c985644-58be-34ad-9d3d-117fcec99c8b | -16.83399 | -57.76845 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| af84de83-37fe-39aa-9c89-97b6100e51da | -16.83283 | -57.75241 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d4ec1fd4-ea3f-37b4-a73e-d64f74cbe18c | -16.83226 | -57.75628 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ff380f78-e96d-39ea-8b6d-d2a3041a203d | -16.82825 | -57.75961 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2da2491a-c39d-3bfa-bbd6-a4214aa4de80 | -16.82484 | -57.80655 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fe4e82b6-6bad-36e8-a9d6-2b1f137124bc | -16.82305 | -57.72307 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3c7fa761-b2b9-3e8c-ada0-197d4335b7f1 | -16.8214 | -57.806 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e3c79632-7774-3f27-997e-ea4cbf7eb33a | -16.8196 | -57.72252 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9de8e847-3695-36b5-bd4f-0117b8877e42 | -16.81853 | -57.8016 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b2d925f5-a38d-397f-9697-4af261602c5a | -16.8174 | -57.80931 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9f30a75b-038f-350c-85d3-a58a9728d090 | -16.81624 | -57.79332 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 44e6a717-6207-352a-9dd8-64e1b90ec0b9 | -16.81567 | -57.79719 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| fc9f7b1f-883a-3650-80ad-9dc6fac06eb6 | -16.8151 | -57.80105 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| efd83d20-4183-3822-ac2e-380883b98e7b | -16.81166 | -57.8005 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9bd4debe-6673-3a0c-b189-fc2e95bb7237 | -16.81109 | -57.80436 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1fca6e42-eaa8-3785-a740-18f310c96115 | -16.80404 | -57.68424 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0b52503b-d167-35e7-82f3-09aa4c181cdf | -16.79108 | -57.8209 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f7256f15-6b73-3995-8c87-4eefe90a5b08 | -16.78764 | -57.82035 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b64f7169-233c-363d-8904-2bab8c95709f | -16.78421 | -57.81981 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3fe25fe0-ee58-31dc-bb93-9a0b0afe3f38 | -16.78364 | -57.82366 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d8660aa4-8a7b-395e-8cc3-5cf64ed5d069 | -16.77334 | -57.82201 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6a75e632-c058-3eee-a060-fa94f271b03a | -16.77143 | -57.81883 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 53698bb4-8934-32a1-8d40-6d8e9baf44e1 | -16.77086 | -57.82268 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a669d6d-8904-30cd-8c23-245f3db954c5 | -16.77047 | -57.81761 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c2b6e3e4-6f71-3f58-8e55-d3ac7acac4c1 | -16.76991 | -57.82146 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 48a2407d-c290-3907-997f-8a3d8ec72cad | -16.76858 | -57.81444 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 357f0317-054e-3751-8953-3ddfe560bea4 | -16.768 | -57.81828 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ab1ae4d5-cb0f-31a4-a1af-6cd5f479943d | -16.76514 | -57.81388 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fa3c5d8a-a82f-3c80-8c48-ba081598f6de | -16.76288 | -57.78194 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 78a341e4-c845-3fd9-82f8-4b3fef61e526 | -16.76171 | -57.81333 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bf7013c0-80ad-3ce5-84c7-a0cd58d4d439 | -16.75943 | -57.80509 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a5f89f9f-532d-3e84-be97-0fd6ceeaaca3 | -16.75887 | -57.78525 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 33ecd01c-67db-36ce-aeb8-6e3509118242 | -16.75885 | -57.80894 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fc233eac-4ea7-38f9-8144-af511875e13f | -16.75542 | -57.80839 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |


[Clique aqui para ver as próximas entradas](README153.md)

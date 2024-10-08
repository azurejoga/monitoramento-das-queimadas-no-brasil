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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbd0e61c-8e64-316e-9e9f-bff4865e72b4 | -4.8212 | -50.81752 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f81b4b4f-5d80-3bbe-b75d-1484d82f26e0 | -4.82059 | -50.82155 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21dd9e14-4beb-3343-8e35-0c9c49a5a695 | -4.81762 | -50.81697 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07490566-ca41-35b6-a180-6ce897f8954c | -4.46292 | -50.50426 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b3a8854-c8be-3d09-a277-0bfe0219525e | -4.42292 | -50.78697 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec60909e-3ca5-3d56-8e6b-be53426f32e8 | -4.41935 | -50.78642 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4bd9be5-ad62-38b1-ac73-b896afc1a686 | -4.37457 | -50.81667 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22e60d09-4453-3ee7-a35a-b2ff01290f1d | -4.17167 | -50.75477 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f1b8734-ebde-3d40-b3ab-38efe871847d | -4.17106 | -50.75876 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58f8b7fd-d2d0-3926-ba80-e88782f7aac3 | -4.16871 | -50.75025 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9e3f41b7-6bd0-37da-ab99-8e0c7964a537 | -4.1681 | -50.75424 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 684aef27-5c39-34e1-831b-695c34f9f4fa | -3.98334 | -50.55027 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42b11333-ade7-3113-9b91-663c7ac46a4f | -5.00697 | -49.59342 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9567e61-40c3-35d1-bbcc-16204a1c6e17 | -5.00314 | -49.59283 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5fd124ce-ebae-32d0-85e7-e566e5f802c5 | -4.95261 | -49.64286 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 530263fe-010f-3a50-8ef2-b9bf9f24f200 | -4.95014 | -49.64531 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd4b6d4c-161a-3486-baa0-3d5969597dbc | -4.9488 | -49.64222 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6c4ffa8-4034-38fe-9015-c84158544113 | -4.87133 | -49.95637 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa40a759-d7da-3c00-b722-f43fa6d77f41 | -4.82718 | -49.8156 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c9ae689-b342-3ed0-b1fa-70d2720051cf | -4.8234 | -49.81502 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e737215-f3b6-338c-8794-e3f7b83cb0de | -3.95057 | -49.95877 | 2024-10-08 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76aebc1c-bfa6-3de5-bfea-4d59fca4afef | -3.94685 | -49.95827 | 2024-10-08 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75741853-2262-3e0c-8c48-ed2495445a05 | -3.9462 | -49.96262 | 2024-10-08 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b6c1cbb-6b37-3687-840c-d1dbad3b90a2 | -3.73264 | -49.68753 | 2024-10-08 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91e583ba-8823-351a-b886-0b3574d94c72 | -6.45053 | -49.87618 | 2024-10-08 04:55:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0083b358-4e46-339b-b41d-68b20bdd321b | -6.44669 | -49.87551 | 2024-10-08 04:55:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 163fbff3-bec8-3e90-8fe1-0c0054794e3e | -6.44599 | -49.88032 | 2024-10-08 04:55:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37692134-b031-3671-88c8-d0709dbd18e7 | -5.84042 | -49.81359 | 2024-10-08 04:55:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f87f52f-af57-34cf-aab0-390e8714e946 | -5.4219 | -49.9593 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec68a4d-c417-324b-b08f-3883427b2abd | -5.41813 | -49.95873 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d96facc-d21b-3935-aae9-d3423b81ae00 | -6.09783 | -51.08987 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b3d645a-5572-3413-9043-12eaf8fc1b3a | -5.49487 | -51.07322 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4331ae10-3c63-32a3-8554-7b748d23bd9d | -5.49191 | -51.06869 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 862d9d1c-5cdb-39d7-b59c-8bbd83e571b3 | -5.49131 | -51.0727 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351929f8-c677-39e5-b86b-dafe5d46feae | -5.463 | -50.66278 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7358446-1b70-3048-bebb-3e5d820a7294 | -5.46237 | -50.66698 | 2024-10-08 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6560f21b-a16b-3961-a866-4a0f6bd74378 | -5.29477 | -50.21887 | 2024-10-08 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fa80768-dc84-3920-9516-0dbd53c939fb | -5.25856 | -50.87932 | 2024-10-08 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a895485-a45c-3f6f-9f38-b0093d8f84b7 | -5.06878 | -50.65993 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b1b2bf97-6fe6-358c-aa10-592517f84041 | -5.06815 | -50.66409 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f07d1fe9-ca54-39c8-a15e-7419df56d285 | -5.06517 | -50.65937 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9747733f-d224-34ad-85b7-86165fe5b36b | -5.06453 | -50.66352 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c3f6f7-05ef-3fcf-9663-f50b814f076a | -5.02902 | -50.87213 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5164a799-e668-3e48-aeb8-e9da5d98b6ba | -5.02678 | -50.95837 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8a57c32-8e39-352c-90b7-e66231605477 | -5.02544 | -50.8716 | 2024-10-08 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fd0345e-d7d9-3969-bf52-9f952a266bb5 | -2.14067 | -50.70294 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25749aba-f35a-32aa-a790-b3261d2e7cfd | -2.13716 | -50.7024 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19e34c9c-2327-3fe6-bb6b-601807c743f4 | -2.12102 | -50.8061 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bbc6685-9702-3fdf-9ad5-c770dae41de1 | -2.09112 | -50.67553 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc95b0a-7ef7-35d0-bd87-74700ea7db2f | -2.09025 | -50.67625 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e572d38-56ce-3df5-97e3-92399075c087 | -1.82707 | -51.05531 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17cbe40d-0b73-3aad-94a7-630439ee7ce6 | -1.6916 | -50.41503 | 2024-10-08 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7689d2cb-e5ba-3428-9141-a218cb03a22d | -3.63144 | -51.17308 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f565cb7-58b9-3474-a88f-de2e43e83d4d | -3.62795 | -51.17255 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5ccf1138-0050-335d-9a17-f96f36e654b1 | -3.59648 | -51.37324 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39194bbb-eda7-3507-a509-0ea0e68a62ec | -3.59589 | -51.377 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 224ce50a-0566-3c53-9f68-a0e294b626d2 | -3.59303 | -51.3727 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e602e97-4a41-3b88-b113-7de4d8d2639e | -3.48587 | -50.81068 | 2024-10-08 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad73b571-a005-3c56-af35-85c04fe56e8b | -3.47377 | -51.37414 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86bd1b1f-b295-3b5e-8d62-0294203fd829 | -3.47318 | -51.37791 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 114419d0-1e01-309d-aceb-0a82cb9864a8 | -3.45747 | -51.20552 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1e427df1-45d5-3756-8ebd-026fd948fc4f | -3.38642 | -51.45996 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 5fecd544-2802-3050-bfda-34e529f9488a | -3.38299 | -51.45941 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 60ddf487-6e94-31cc-a03b-8fcab5d76331 | -3.23682 | -50.83915 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f39daa95-722b-37fe-94e3-186f24f43bee | -3.23622 | -50.84303 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a2f172f7-829b-3991-a302-daafb197c8ff | -3.23561 | -50.84692 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9127edee-b7f4-39c5-983c-6410f22f13fc | -3.22057 | -50.92011 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e11d2f9-30e6-36d8-a02b-025139b1c71a | -3.21706 | -50.91957 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 453d074b-58d7-3dd4-818a-92d623e8f176 | -3.14515 | -51.19811 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfe6f8d6-bd5b-3bb7-86e7-87afb0416b4b | -3.05215 | -51.09921 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 291b944f-e7eb-3966-97eb-be62606a4dd1 | -3.052 | -51.14587 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f188d94-3064-3dab-b6cc-741cbc89fcbc | -3.04926 | -51.09492 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 847ff8a1-a396-3570-a37d-2a287d39e606 | -3.04867 | -51.09869 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c2c34e4-2b2c-3d90-935e-c6e4004522ef | -3.04854 | -51.14533 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 761408dd-2c2d-3fec-a4b9-415efaea5482 | -3.04795 | -51.14911 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c2e06ae-584b-3e2f-a986-20805d469680 | -3.03708 | -51.10467 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 906cf29a-242a-3012-90ff-b9e4e6aaa62a | -2.97634 | -51.03006 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67977791-0759-3022-a619-e3a426cbb4a3 | -2.97346 | -51.0257 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc778ce-483a-3beb-b0aa-92683a35e25f | -2.97286 | -51.02951 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3848664-e040-3c16-ae5a-4f928a2d4f4a | -2.97082 | -51.11088 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 670d1511-0655-3ba2-a466-8ead05408f66 | -2.96938 | -51.02898 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af7476d3-f9c4-3dee-9659-96988eb224fa | -2.89705 | -50.70539 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e75e16f-fb54-3ac7-b969-a7680abaf147 | -2.89645 | -50.70931 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a840415-0b19-30a5-8dc7-bf4c2eeb2143 | -2.89584 | -50.71323 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ccb58d6-3784-3d29-8896-f1ea3ebd6593 | -2.89231 | -50.71268 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b1140a2-6fe2-3174-b0ad-7e356daaf3e5 | -2.8894 | -50.70823 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2817d51d-1b76-3f6f-92fa-a7649e0bb069 | -2.88587 | -50.70769 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 052b40e3-08ec-3e52-a5b1-350c94d9515a | -2.80789 | -51.39219 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a2e9a5d-3de2-393c-b2fc-021bda0cea52 | -2.55837 | -50.63651 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e18e04d-5b4e-30b6-a676-5d889d2b785d | -2.32016 | -50.52198 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85674656-9450-3e03-bdb5-55443e68dc5a | -2.28406 | -50.54461 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 581e3818-1250-3524-9418-b20b7e2ca46e | -2.28344 | -50.54855 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1eb74a35-7f66-363f-89dd-0dfd52206cec | -2.26523 | -51.24657 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2974b177-f752-32b1-9b3f-026706a085fa | -2.26373 | -50.60562 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d390336-4013-38a9-8d55-af285d6e1a70 | -2.26312 | -50.60952 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82f603ea-ebd9-3ee0-b631-af5e8b5bbe90 | -2.58392 | -51.82372 | 2024-10-08 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c5ffbd0-83da-31de-8f69-7f693d58f356 | -4.65315 | -50.94987 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3560168-dca4-35d1-ad95-d6dde23a0490 | -4.6496 | -50.94935 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2388d8d-8fbe-3c2a-9d96-2d1a4c270907 | -4.63513 | -50.97665 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ce9bbd7-e13f-3525-adc4-2264d0e2b000 | -4.63476 | -50.97549 | 2024-10-08 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README82.md)

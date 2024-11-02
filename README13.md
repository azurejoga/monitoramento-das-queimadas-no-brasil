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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57537b2b-b163-38c7-be5d-279ba6c996a3 | -4.23682 | -48.55028 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 074e4dda-6487-3e61-bf55-e369944e0a09 | -4.23474 | -48.06873 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 94eeb0cf-6137-392a-a111-b574708fb56b | -4.23358 | -48.72164 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0e209c89-3295-39c1-9e74-0e7de4621674 | -4.23351 | -48.05993 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45f66881-4b19-349d-804a-c3d7d903a6cd | -4.23227 | -48.0511 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf7c72b0-f7b9-3f3f-9bd3-1c4d2337bf9b | -4.2292 | -48.56034 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e4359a8d-6e95-3241-9ff2-61fbb443bc1f | -4.22798 | -48.55153 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 74fe770c-a6f9-3522-bb1a-f7f39b8801cd | -4.21031 | -48.55403 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a8ae6e12-21a1-3594-9e76-89df22ba3427 | -4.12445 | -48.27626 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb2fc1c4-772e-30f8-bcfb-b411fab600a4 | -4.10333 | -48.51263 | 2024-11-02 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cc70f663-2dd6-3834-9f59-7c02c4edff24 | -4.0852 | -48.31773 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 45831e38-2fb3-3ef9-82a0-7badec9f4d4d | -3.96306 | -49.03729 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d6dd49f6-8ba0-3182-aa7d-016466bc66a1 | -3.94391 | -48.36792 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 90b94e38-0867-32e0-8b0e-cd91ec23887f | -3.94268 | -48.35912 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 119cbda2-1ce1-33c7-8fed-7a4c879cb106 | -3.94145 | -48.35032 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7e781d0e-bf86-3494-a650-3847facca863 | -3.94023 | -48.34152 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 14140677-883d-3a0b-b96d-5cdb30a78c99 | -3.93385 | -48.36037 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 7df0cc95-4dd2-3ed3-83b5-784e34775b4a | -3.93262 | -48.35157 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3382aa5a-bdd6-3196-a18c-9d6cab56bca0 | -3.91276 | -48.93573 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1d8a9ffa-ffa3-3d78-9466-b84cdf1639ce | -3.91153 | -48.92687 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 306980cc-2bfe-3a4a-9c86-ec08262e8c98 | -3.90858 | -48.37292 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9081708-489e-3a3f-b453-5a0ac4b001b3 | -3.90267 | -48.92812 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 888465b3-c129-3fc4-9d81-563441de6eb8 | -3.89975 | -48.37417 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bc044815-b1c1-3916-9847-4295ea40a72e | -3.89852 | -48.36538 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 054d5962-c9b2-3c62-9d81-f354b61c23d7 | -3.88969 | -48.36662 | 2024-11-02 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4177b766-faa5-30bb-8683-1a30e0f06f24 | -3.8323 | -48.89016 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b85f3f49-a856-346e-9513-e03ff9b9b703 | -3.83107 | -48.88131 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 482bfacc-4b4b-35cb-9212-2490c3ab7d1a | -3.82689 | -48.98125 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| b229ba06-7864-3e3e-be5c-c47add598c14 | -3.82566 | -48.97237 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 31b75f5b-b338-3c6a-ad62-53fac463383d | -3.82443 | -48.9635 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c7b11bbe-e445-3d38-9d87-5bd6ae75de79 | -3.82345 | -48.89142 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2f6e71e-491d-3098-9170-bbc57f0438ad | -3.82222 | -48.88256 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d5ff208f-6a27-38d2-8216-6429587d8097 | -3.81802 | -48.9825 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ef9b33b2-afef-30e7-88a1-ef013be0d28b | -3.81679 | -48.97363 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| b2c3e00f-b4cd-35b8-b4e7-8aac87a3aeb3 | -3.81336 | -48.88381 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 51a98608-eedd-3abc-87a3-99a9b9370b94 | -3.81213 | -48.87496 | 2024-11-02 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c46cefe8-5124-319e-9dc3-4b5b77440d51 | -4.93367 | -48.51995 | 2024-11-02 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8963763e-299c-3f0b-87cc-32839ed6f29b | -4.93245 | -48.51112 | 2024-11-02 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d711311e-e6c9-30bb-a05e-cc2e5a5809aa | -4.92078 | -48.63623 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b33eecaa-df69-3e0b-b996-39d5515ff372 | -4.88659 | -48.65007 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42936a34-4b9f-397d-9fcd-9e978316615d | -4.88241 | -48.42537 | 2024-11-02 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e3a67bf6-9476-3cd1-b596-be754ab2d5a5 | -4.87799 | -48.5881 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8bdf9efd-77b9-3b4a-9015-b6e082f88bc2 | -4.84899 | -48.57417 | 2024-11-02 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 29e0be5e-4eb3-3e64-a328-d718ff719f44 | -4.84137 | -48.58423 | 2024-11-02 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c22e1907-f7f5-3964-aad9-8bab69b9131c | -4.84014 | -48.57542 | 2024-11-02 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 210d4b12-8efb-382b-9837-d0df0bc1040f | -5.7126 | -49.22805 | 2024-11-02 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 63fa6eb9-ab46-3cbe-b666-f7fede6f35ea | -5.23267 | -48.08431 | 2024-11-02 00:54:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ad6de35f-6af4-3f77-82a0-55ea4aa7322b | -5.23144 | -48.0755 | 2024-11-02 00:54:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2d71cb22-c810-3568-9e9a-c75bc8c458f4 | -5.22384 | -48.08557 | 2024-11-02 00:54:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a75abfb6-d02b-3361-8d2f-60af966b54e6 | -5.22261 | -48.07676 | 2024-11-02 00:54:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dbe84f7-935f-3a6e-8379-a37da6017b28 | -6.3944 | -49.56634 | 2024-11-02 00:54:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 31452246-5782-3d34-a9b3-74ab43985034 | -6.38524 | -49.56762 | 2024-11-02 00:54:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b58b7dc-3b36-3d36-a86b-a230f5cf9cd1 | 0.08718 | -49.86354 | 2024-11-02 00:54:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4146a450-c47b-3d24-9558-4f3982724874 | -2.24202 | -48.84963 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5ab6458-e787-3a78-ba26-cfb99e805dc4 | -2.23319 | -48.85088 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bcde452e-8359-3683-9d1b-cb3c32b5a80a | -2.22698 | -49.14503 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bc6c4ee1-1e9c-3aff-9956-fa3a0fd1cfc7 | -2.21814 | -49.14627 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 684be89c-9a94-3f58-b680-0b8854b489d5 | -2.21691 | -49.13745 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 67cf46c2-1b0d-3dd2-895c-11ecca6255a5 | -2.21052 | -49.15634 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7b857dbf-7c40-3775-ad4c-981a3751d7be | -2.19651 | -49.1853 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9252107c-1b00-3bca-9e06-175fe743af9f | -2.19528 | -49.17647 | 2024-11-02 00:54:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af8c7bda-580e-3920-9cc8-2c1644502ca5 | -2.15384 | -49.54086 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 618603e3-708b-3189-8870-1f332c8b04e1 | -2.1526 | -49.53193 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 3923837e-509f-3e6e-8bde-a2dbb541bec0 | -2.1437 | -49.53318 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8b5c53b3-2011-303f-940b-0eb83bb48c42 | -2.14247 | -49.52426 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 29c431c7-8ba8-3dc5-b3b6-22c685a645dd | -2.11315 | -48.90991 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ed1e9f5f-27dc-3b46-a779-fd2447a3a81d | -2.05922 | -48.86069 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9181d2fd-6af9-3e6f-adbe-ed4568fb95a0 | -2.058 | -48.85191 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 88e1effe-6a28-3644-96ae-9da73a3e109f | -1.12724 | -48.7218 | 2024-11-02 00:54:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 13818339-6897-3449-aafe-813257059d16 | -2.04079 | -49.71832 | 2024-11-02 00:54:00 | TERRA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45cd96a9-7404-3916-8308-5474e4ca0e46 | -2.84336 | -49.86217 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ed997ddc-71e9-381f-a246-abbdeea962b2 | -2.82172 | -49.77206 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 674fe72f-2932-39f2-a67f-d80743388920 | -2.82046 | -49.76299 | 2024-11-02 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b49f312b-1526-3fcf-ad72-ce747ca983af | -2.66565 | -49.84331 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d3bfc9bc-cf9f-33e2-8fa4-609d2fa5d963 | -2.66438 | -49.83418 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88a1ad0a-5a1f-36e1-8d63-80692cb49104 | -2.65666 | -49.84456 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 40f8bcf6-5001-3eb0-910d-0954419c79d4 | -2.64767 | -49.84582 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2879f913-6271-3d72-8a56-93dfbe29301f | -2.64372 | -49.88364 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| be53fe93-c8ed-3167-b39b-c60b3ed2fe08 | -2.60794 | -49.82352 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3c0a4665-55a5-3f5d-b5a5-f1152b5bcf14 | -2.59802 | -49.82148 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 11721f3b-eda1-3d9e-8e6d-51fccdba3503 | -2.57581 | -50.05855 | 2024-11-02 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 48526e9c-6a6d-3dff-b067-6bfe27273534 | -2.56475 | -49.7798 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e9fbd119-4a9c-3cfb-935c-071fc6c63e06 | -2.54966 | -49.67122 | 2024-11-02 00:54:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93403b00-a214-3ac1-9fc2-8858b50301b3 | -2.5479 | -49.85637 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8fbab7ff-932e-3ab3-ac9d-60e9d51c0638 | -2.53118 | -49.86802 | 2024-11-02 00:54:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ff26d23c-cc8d-31d1-a8fc-0b383e47b4bc | -2.62236 | -49.19372 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 56bcebcb-0013-3c39-8446-7351faabc403 | -2.61358 | -49.27361 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27038c93-b642-3114-9577-1157cd5f6bd3 | -2.60245 | -49.19388 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 91a57148-082e-3874-b816-49ecd7f655fd | -2.60223 | -49.25711 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47eb8022-7cf0-3793-b781-f923db5ee265 | -2.601 | -49.24825 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f7fe499-2e1d-3ba3-b78f-5318b39f4cd9 | -2.59359 | -49.19513 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4aa0c917-7576-314f-b9b7-4751789a489a | -2.59291 | -49.38525 | 2024-11-02 00:54:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| df793617-b447-395f-91e5-7f043b1276b7 | -2.58966 | -49.23178 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 71f0fdf0-63c7-3b7f-a22f-b5b842c0a8df | -2.57488 | -49.12566 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 10f56f1d-796f-3acf-b0ed-9b0a4a83c8ea | -2.57365 | -49.11683 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 516f7f42-fb86-3995-a1cd-f47b09bdcdc8 | -2.57169 | -48.97329 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 080f2617-4380-3614-a303-b370c10d0b37 | -2.56874 | -49.08153 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23fa58be-2004-3bec-a9a5-6146e7a84f02 | -2.5643 | -49.24438 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 6764927d-ba3d-3ca2-bfe2-ae66795084d4 | -2.56184 | -49.22667 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d50d84d6-b049-3361-b426-4df464e6fb9e | -2.56061 | -49.21782 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README14.md)

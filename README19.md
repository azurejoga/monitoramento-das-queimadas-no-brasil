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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d649c59-4825-3f24-b8ba-2401f7f5e083 | -12.19989 | -50.75597 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8534cf94-2f29-34fa-9a43-a5869eadca9f | -14.52124 | -48.33918 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85ca7e85-f2cf-36d9-804e-62153eaa8b7b | -14.68036 | -48.75928 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bf41e6c-5288-3b06-b87c-75532c4d23c4 | -13.45489 | -48.63507 | 2026-09-25 04:27:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ac3ce75-aa9f-35c4-92c9-3904833f2656 | -15.4959 | -41.55014 | 2026-09-25 04:27:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6e0458ec-1c05-38f8-a939-80023cfc9ba7 | -13.20395 | -40.45895 | 2026-09-25 04:27:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 114808e1-bf7d-3c2f-8a37-0d10aa246fdb | -12.05741 | -39.0132 | 2026-09-25 04:27:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 04b4cb48-6929-3d06-b692-5263b6d446d1 | -12.18944 | -50.79181 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0cdced49-d256-3c74-99c9-dec9536fa933 | -12.65309 | -43.16517 | 2026-09-25 04:27:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 062493f3-a52d-3f23-a9f3-3860537d657d | -12.19711 | -50.79546 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bc00c517-e67c-3905-adeb-a7b40e1f5357 | -14.72224 | -48.76518 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 513f1951-3bc4-36db-9901-65ee4301087c | -13.70895 | -48.80062 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d2f332d-5068-3dc4-b140-7e954cac5b4f | -12.1991 | -50.76025 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f7e8f73-2167-3fdf-8056-e4a68cf02545 | -10.29337 | -49.95716 | 2026-09-25 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ebed2ff-2b55-398f-9ab4-d1961399b5e3 | -12.20587 | -50.79712 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29b24f7c-73a7-317d-b122-13ed1655e682 | -14.51834 | -48.33422 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6972a78e-7bcc-35d0-9750-c385aefd90d0 | -14.37482 | -47.24841 | 2026-09-25 04:27:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c876ec9-8eb3-3c04-a8c5-ef48aac089d0 | -12.1987 | -50.78685 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e46e48e8-61e1-33c4-8cf1-2e1e985034c8 | -16.11677 | -49.94726 | 2026-09-25 04:27:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3da48a35-5fdf-382c-b514-3d63304afa1f | -10.8843 | -45.07838 | 2026-09-25 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceb5d699-ab63-3824-89b7-7c6a41858419 | -10.6173 | -53.99312 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76b45a89-207d-3db3-a522-c49c98e02900 | -10.90447 | -53.93953 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c23288-49a7-3e53-b330-4e8af11b6058 | -14.72051 | -48.77135 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75428933-dba9-3aab-9f1d-cdf380ec9a54 | -12.19654 | -50.72656 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 356d4906-501f-38ed-b0f4-4feed12b7ed6 | -10.90102 | -53.92768 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5af8df5f-44d0-3096-9e2d-59b6db4b5546 | -12.19592 | -50.72868 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 15896c31-51fc-3e7c-8ea7-1b40ca17544c | -15.07422 | -52.80025 | 2026-09-25 04:27:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e15d41-87bc-3563-b7ac-35e9e3db0b69 | -12.22253 | -50.75585 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7800993-869c-3df2-9587-b6a9e670043b | -12.20585 | -50.74825 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 53a3c846-f410-31e8-bb2b-ddcaeb33f448 | -13.71728 | -48.79758 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf284428-27f2-3f19-b775-212549d7ccca | -12.19404 | -50.76595 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02c8a47f-9dc7-3629-8716-2b27dfd364c3 | -10.41914 | -53.78044 | 2026-09-25 04:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc2776d7-83a5-3eab-aaaa-f4a40950e893 | -14.40188 | -41.61601 | 2026-09-25 04:27:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c67e8c02-0796-30d2-b15e-d26f9396546e | -14.76624 | -48.47383 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a1acf4b-5c51-3eca-8ce1-3a6af937b031 | -12.19535 | -50.78402 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 806db61e-730b-3223-b540-df0c13ff540a | -12.9024 | -47.24051 | 2026-09-25 04:27:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca154fa7-c666-35d5-b572-c06500bec312 | -10.61871 | -53.98562 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 710174af-53de-324f-9b69-216e121dc06d | -12.20222 | -50.74535 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f69636e4-e5de-34e7-a5d4-94ebabc84abe | -13.73211 | -48.97562 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48fc4f2c-2714-386f-baaf-426fc0727682 | -12.74791 | -47.78191 | 2026-09-25 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13555e33-5002-3acb-a20c-9824989f8e57 | -12.20029 | -50.77826 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 525e8ada-9c1d-3566-be7a-2e4711923fb2 | -14.51467 | -48.33367 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b19012cd-ff4c-3d1c-8a56-099079c0bc06 | -10.62355 | -53.99054 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edfe8e9b-ea2f-3779-b910-9a6d41854d32 | -10.62271 | -53.98564 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f673033-caab-3ba8-aaff-95968d53d7ee | -17.10468 | -46.47026 | 2026-09-25 04:27:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30069c15-8753-3599-a1ca-b8112f7cd3e8 | -12.1995 | -50.78255 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63f49843-c620-31ce-9bf0-3268f3e4c929 | -11.6652 | -43.75802 | 2026-09-25 04:27:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd350975-ec79-3490-a47c-43e04b80c943 | -17.76642 | -46.63039 | 2026-09-25 04:27:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3272ce93-568a-3118-ba63-97b4a1b653cf | -11.61701 | -50.58947 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f85e568-9663-3a20-8d46-1ef4f86889ea | -12.22052 | -50.74219 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7ac7a3b-c297-32f1-811d-a27355f69d27 | -10.90236 | -53.95057 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c1c1cf-da77-355d-9aba-488d4465a13f | -12.20626 | -50.77049 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bffc6dd-c0af-3895-bb8a-0446ceb7f76f | -10.2848 | -49.95558 | 2026-09-25 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecf9c406-c933-34f1-9e14-91879dc209b9 | -11.37335 | -43.38363 | 2026-09-25 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d92a89c3-3fd7-31a0-bc0c-4c5d969f7fe8 | -12.18966 | -50.76512 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccfe4baa-5192-31c3-80dc-6fc8b4eba543 | -12.18015 | -50.76774 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67e9d941-08fc-3dc5-a72b-7cd7b2275bbf | -12.20146 | -50.74963 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cbc8b0b-1cb8-3e52-8f6e-3a534ec94810 | -12.18682 | -50.7557 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e5ea82e-9568-30b1-8e27-bec0cab40118 | -12.17475 | -50.81802 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c59951d4-81d4-30f8-97b2-476c7dae08be | -16.70074 | -50.66639 | 2026-09-25 04:27:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c841525-2529-3be5-ae0a-a048753fc687 | -13.70519 | -48.79985 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ffd9ba5-e59b-348f-b1c7-49155a8753d9 | -15.81148 | -53.11096 | 2026-09-25 04:27:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fea64b80-6e43-3362-9720-20a6ee06c569 | -11.2856 | -51.29762 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b6cde12-d120-3ecd-900c-78ff4e567cd5 | -12.17036 | -50.79709 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2fafb043-125e-3397-9e12-e2dc1b90c3e2 | -10.28909 | -49.95637 | 2026-09-25 04:27:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3866b8e-cbab-3263-b669-2f6becb1742b | -10.62285 | -53.99428 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d64e83d4-deb3-378f-8280-ba0211f7008f | -12.18396 | -50.79296 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 17645b3e-aae4-310f-8245-362a0877dd56 | -12.21974 | -50.74646 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0254d099-4fb3-38c5-b706-25cb7ad69efc | -10.89682 | -53.94954 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d9ee07e-0f64-3560-b73b-5f1606bb5718 | -12.20109 | -50.77396 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa198ab6-88be-3b62-9f73-ec52c21a28de | -12.19097 | -50.78318 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 20967868-2a0e-3505-b9da-dffc4710a16d | -12.19633 | -50.75308 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ef4fa34-4e48-3d8a-96d9-93f866ed58ac | -16.0045 | -56.31884 | 2026-09-25 04:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 8ff6c313-b323-3345-9bc0-24b6840df4ba | -10.89824 | -53.94217 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6078a048-af4a-3607-a1c1-20df367746b3 | -12.21379 | -50.75418 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 381c1344-1ced-3ee6-8b47-c7f7167581cf | -10.61423 | -53.99948 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2255037f-2cbe-3402-b325-31ce815b3e20 | -12.19841 | -50.76679 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d4fc7786-e33b-31ad-8b77-0622b37f2b4f | -13.70601 | -48.7951 | 2026-09-25 04:27:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65b4abf9-e2b6-370a-9969-67504f4d15ce | -12.2009 | -50.7274 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3acd1094-8656-3f8f-9d61-4842207ce6aa | -11.71738 | -43.46718 | 2026-09-25 04:27:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ee927a8-bd1d-377b-87ed-c508c5ca8b17 | -11.2948 | -51.29938 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| febc92f8-c00c-3bde-a100-2725d3eecb9e | -13.17899 | -48.53267 | 2026-09-25 04:27:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| feecef8d-36dc-3e16-b866-d903afa26b81 | -12.19831 | -50.76454 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 81aa12c9-d7f3-30e5-90fd-f6d423fc9d30 | -14.51758 | -48.33861 | 2026-09-25 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57cd5c3d-5e82-3a6a-8b7c-c98c5bfbd805 | -13.06855 | -43.27495 | 2026-09-25 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 871da4d8-9701-38c8-b5c2-61433fb5570b | -10.42464 | -53.7816 | 2026-09-25 04:27:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2273c5b2-c4a6-3fe6-89b4-61c71d4911aa | -12.53811 | -50.06877 | 2026-09-25 04:27:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c95308ae-150d-3506-8759-a12c7f9776e5 | -11.62759 | -41.83359 | 2026-09-25 04:27:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7fc9e924-3e88-326d-b5da-c3730417b06b | -14.72143 | -48.76978 | 2026-09-25 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d30fc602-13dd-3198-9813-7170da417378 | -12.1889 | -50.76942 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a66716b-b5e7-3c39-b274-03ff48dc09a9 | -14.06563 | -44.06226 | 2026-09-25 04:27:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a953836b-77f6-3e94-98b8-ad8537757e28 | -11.77085 | -50.90746 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c2878be7-f599-32dd-bf12-166d90eb2f68 | -11.2902 | -51.2985 | 2026-09-25 04:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 317a6a6d-85d8-3344-ad04-0760bcb320e0 | -12.19021 | -50.78749 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 314735a8-da1b-31c6-a425-2d134e78fbd2 | -12.54982 | -50.07865 | 2026-09-25 04:27:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c98b3b62-af2d-3417-bd3b-582a1219f9e4 | -12.17319 | -50.80659 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee098f1c-2936-3930-8493-76f07a59dbef | -11.15899 | -50.65287 | 2026-09-25 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5b69751-1a61-3d91-a87f-e85af9e7cb49 | -12.18834 | -50.79379 | 2026-09-25 04:27:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f2d8af50-f8da-3759-8717-1bbe3253a6a9 | -10.90033 | -53.93127 | 2026-09-25 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a43b8f02-e004-38ef-8e8d-4e2bc69b7651 | -13.40382 | -40.96455 | 2026-09-25 04:27:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)

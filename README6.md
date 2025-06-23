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
| e7a45143-1f13-38bd-9f8b-7820c08eb378 | -10.98314 | -47.40686 | 2025-06-23 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f4c9d06-d9ba-3a62-b42b-a0ffec532077 | -8.3952 | -47.1423 | 2025-06-23 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc5c14d5-9ffd-34e7-91c4-50bcff0e1cb9 | -7.45047 | -45.5596 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8145402d-b510-3d39-89ce-4d689c66a326 | -5.11018 | -43.14695 | 2025-06-23 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| efa0ecbb-68de-3895-b1c9-389154f0dc60 | -8.71895 | -48.01443 | 2025-06-23 04:21:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e07757b2-948d-338c-a375-7c1ed0f0af69 | -6.85775 | -43.15029 | 2025-06-23 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5cf7052-aa9e-3f59-8211-bdb115ed8807 | -6.97175 | -42.93276 | 2025-06-23 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e72fc62-b62e-3644-93a0-d76a41f04a5b | -8.11033 | -43.14766 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 88aee5ba-9488-38fd-9253-b67fa338eef1 | -8.065 | -43.12144 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ca4e0709-59ea-3aec-b219-9529c5a432b3 | -10.03862 | -48.67729 | 2025-06-23 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62e660f1-5017-3592-9bca-46b617128182 | -8.11377 | -43.14819 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 49a999ac-970f-3c96-bceb-48d118a49371 | -9.42151 | -48.41405 | 2025-06-23 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8a6597a-fafd-3f0e-ad75-e7b13a711fcf | -8.11721 | -43.14873 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| eaee3470-c819-3a8c-9ea4-2eb46fcfc56f | -10.29102 | -52.56425 | 2025-06-23 04:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12775821-6a49-3d09-bcb3-352802519a73 | -8.11435 | -43.14444 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 34260c4f-c5ff-38ca-a07a-973fc819d597 | -10.10684 | -50.9365 | 2025-06-23 04:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b49b257-57a2-3ebb-af19-fd0a4e2bb9cf | -11.10354 | -46.66683 | 2025-06-23 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce7d9bc2-846d-3833-8c0e-af5ad4d71b63 | -8.40819 | -44.61037 | 2025-06-23 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a91fadc-a740-3a80-927b-61a4d704a7ce | -8.38766 | -47.44099 | 2025-06-23 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95746cd4-1b8e-388a-8670-d1a8f6da50eb | -7.35821 | -47.74834 | 2025-06-23 04:21:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 293a1005-0d84-3328-aad3-c20902a754ea | -11.50859 | -48.95475 | 2025-06-23 04:21:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9ebb5cd-fa2c-37e6-aebd-58f1734809ce | -7.31149 | -43.21817 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1bcab392-6707-36d5-b415-af28a76f3dac | -8.096 | -43.14929 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8c3c5fe5-7f85-369d-8a33-62e582044a01 | -7.3655 | -43.36541 | 2025-06-23 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e29942e6-865a-3822-bc2f-af903d2bb2b8 | -7.4377 | -45.53244 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dda5e3d5-f37c-3008-9bc6-f50816f784a6 | -10.9481 | -48.22696 | 2025-06-23 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb7ea613-8e2e-3d6f-b6e1-5f3e8eb854b3 | -7.31659 | -43.20764 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5a580467-dd0f-37ac-8f2b-395cb58e080f | -8.06557 | -43.11768 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2aff9443-0da7-37aa-a18f-f7fb706256a8 | -7.94747 | -46.04343 | 2025-06-23 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17a91901-84bf-3265-93c4-0d447b51467e | -7.35029 | -45.3353 | 2025-06-23 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebda02be-cbae-3447-aeee-ab19f21aa3c4 | -8.39863 | -47.14288 | 2025-06-23 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c09fa4d-4833-3dcc-8c72-b3a9bb382e9d | -8.06511 | -43.10698 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 392dbb5e-a9f9-32d5-8575-fbce5b24b3bc | -5.41967 | -45.11113 | 2025-06-23 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2752269b-196a-3008-a133-50b9fadea8df | -11.58272 | -44.65441 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f55378be-82c4-3423-b403-2b6ea10d58f4 | -7.44492 | -45.55152 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c419810-7652-327a-b564-7073ddb2ad5e | -7.44936 | -45.5666 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c21bdcb-feb7-3701-8db2-4fa786d5678e | -10.62516 | -48.08231 | 2025-06-23 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ed87e1e-4422-3d52-8207-6dc1c8a318dd | -7.46491 | -45.5547 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a01b4a26-05e1-3e2f-bc11-2eb1dc6325bf | -10.05738 | -49.66243 | 2025-06-23 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81068135-8fff-32fa-b98b-124bd2563a2a | -8.06155 | -43.12091 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d2e9378b-5253-357e-877f-b4aa119040f0 | -7.36493 | -43.36906 | 2025-06-23 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cad4b10-9192-3e2a-b708-db68f5a36a97 | -7.46755 | -45.55134 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a44694e-ff6f-3d07-8da9-f69500ddfeaf | -8.06958 | -43.11445 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ec7bd0c1-7803-3d9c-a226-e201fd3945b5 | -10.14773 | -48.98802 | 2025-06-23 04:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a6e9d0c-37ce-39dc-9312-4c6302e62796 | -8.06784 | -43.10262 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 94041da4-e990-310c-aded-8041f0234638 | -9.14937 | -48.97196 | 2025-06-23 04:21:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66c879a2-2c64-3950-bfb3-3eec27fe434b | -8.07072 | -43.10691 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a564d834-09b0-3567-beb1-e94fd6e26f1f | -7.44547 | -45.54802 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 129f0d19-a07f-384d-9798-a7c03175468d | -6.89717 | -44.64754 | 2025-06-23 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed8f027c-c4af-3b65-8c0a-ed658bbb5841 | -10.15042 | -48.98732 | 2025-06-23 04:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6481c07-1ee4-32cf-b374-bb10a1d7f077 | -10.57111 | -51.8919 | 2025-06-23 04:21:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e91251e-3e2c-3266-82dc-c57d111224fb | -8.05992 | -43.11773 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8570fd2b-0874-35cc-9fcc-15891f34d3d4 | -7.31261 | -43.2108 | 2025-06-23 04:21:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| af6d28ac-a0d6-3f58-8ece-476c8b60bcda | -7.43936 | -45.56502 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62657e35-d14b-387b-968a-a10677b457b1 | -5.49674 | -43.98222 | 2025-06-23 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df01e9ad-adff-3dc5-8c50-8aabb8cd0d44 | -8.06337 | -43.11825 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c439a41f-acd3-3b42-a4ea-a8aa59b146d1 | -11.57541 | -44.65697 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45377f95-fef2-35f5-bc22-0f07ddcab7da | -5.49729 | -43.97875 | 2025-06-23 04:21:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 930f3314-6d56-3779-aeae-36c52db74a75 | -12.43384 | -43.77327 | 2025-06-23 04:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a45865ee-b2ee-317f-8706-366121f4820f | -7.44881 | -45.54855 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62b7d779-8ca2-3f0b-acb5-4d66d0fabcce | -7.44992 | -45.5631 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 395fd3a9-33ef-3749-8085-1bfd2d746e91 | -11.57823 | -44.66113 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83bff413-d7a3-3d57-afc1-4021b24ca0d6 | -11.57934 | -44.65388 | 2025-06-23 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2dbd5d97-4f6c-3f7d-a13f-4f1588004d8b | -7.09577 | -44.17839 | 2025-06-23 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f843ab68-8fef-3d0e-94ed-a465d6cde88e | -8.06901 | -43.11821 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 26f98f3a-c958-381e-b2ca-1cbc0711d46b | -8.07129 | -43.10315 | 2025-06-23 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d323a21-7a1f-3930-88e3-5ac724a6daef | -7.4438 | -45.55854 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb563b56-8814-3980-8d24-3c40d94ecb55 | -7.46547 | -45.5512 | 2025-06-23 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4b11c32-cddf-3087-b1a5-f4f6bddacfe8 | -8.48531 | -47.5045 | 2025-06-23 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 252a69d6-e112-333c-87ff-340945bc45d7 | -13.26948 | -46.81794 | 2025-06-23 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af7b1ca7-15d9-3743-8c3a-78d34a4a3c74 | -11.18668 | -54.40858 | 2025-06-23 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f59ed417-6f38-3b33-b3d8-fa91d3d30f92 | -12.25146 | -46.68756 | 2025-06-23 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 502e0c75-39db-3337-b5b9-d057a11fc3b7 | -12.19993 | -49.62649 | 2025-06-23 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa60a8ed-876b-3491-bebb-144b73f04369 | -13.75889 | -47.745 | 2025-06-23 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be48aea0-8d1a-3bb8-abf9-db1a0025435c | -13.26501 | -46.82455 | 2025-06-23 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc671b25-dc67-34f0-a56e-98be7bf386db | -11.61662 | -58.28584 | 2025-06-23 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00f27046-be63-3107-80dc-a229e060b7db | -13.02976 | -42.67384 | 2025-06-23 04:23:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dba54de6-6cab-3d65-9c0a-0d5c6538becb | -11.14047 | -53.94195 | 2025-06-23 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2ae277d-76d7-3ee5-8ff7-8be0c42318b3 | -11.61551 | -58.2913 | 2025-06-23 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4feb5683-303a-3a79-b11a-5669af2ff617 | -13.26661 | -46.83588 | 2025-06-23 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7f1d374-f84a-37d5-a1f4-8fb98140bf5c | -13.66618 | -43.66427 | 2025-06-23 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53166b86-65a1-3281-9ee4-a0a06003a52c | -13.8225 | -49.31005 | 2025-06-23 04:23:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b190661-3650-39d3-a940-afe39284b053 | -13.24 | -49.83435 | 2025-06-23 04:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1fc72f8e-d60c-3f7c-93e0-c63286252ba6 | -13.26558 | -46.82094 | 2025-06-23 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5746237b-b1b0-32b2-9db4-c02fdb517733 | -13.76268 | -42.97711 | 2025-06-23 04:23:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ae1e87fe-fed6-3fad-94a6-9af9c963f4ef | -13.27167 | -46.82563 | 2025-06-23 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b8569bb-2aa0-307b-9abf-dc1717a1917a | -13.02542 | -42.67775 | 2025-06-23 04:23:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ca5650a-94dd-3e57-b5df-923302fc5bfb | -13.27558 | -46.82257 | 2025-06-23 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbfca83b-0d09-3e81-bef9-c8a3df75110e | -13.83322 | -44.4578 | 2025-06-23 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a1810e0-c16e-3e4d-9b0b-3e69405129e6 | -11.13553 | -53.94104 | 2025-06-23 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d191d3ed-a59d-366d-a9c8-52464410c427 | -11.62195 | -58.29261 | 2025-06-23 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59aa8e7d-bcb3-308c-b7c6-1b08a921b2d6 | -12.30685 | -53.26722 | 2025-06-23 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe05fd19-d6aa-3f34-beeb-9823b0eb26ee | -12.43494 | -48.12727 | 2025-06-23 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92d79015-3f7a-3351-9c3e-d9ebaa83485f | -13.23925 | -49.83877 | 2025-06-23 04:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c77f1c91-9156-3275-a5d4-6dfa93ecde7e | -13.23632 | -49.83368 | 2025-06-23 04:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85ef1efc-9f57-3244-b817-94813f92d08c | -11.62308 | -58.28706 | 2025-06-23 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3a4d872-6c60-3c8f-a7a7-3bcd043e250b | -13.24367 | -49.83503 | 2025-06-23 04:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bd8fd387-cc11-38e4-994d-3db2b151d7e4 | -11.60907 | -58.29001 | 2025-06-23 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d453d536-c276-325b-896d-255b14346b83 | -13.02606 | -42.6733 | 2025-06-23 04:23:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 834cb2f2-cbbf-3697-9e41-54ec5dea6d10 | -12.19623 | -49.62583 | 2025-06-23 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)

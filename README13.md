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
| aa1ba41b-9557-356c-b86d-2f22c37e49c0 | -16.31069 | -58.25304 | 2025-06-18 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 51d15284-bb12-3944-8a2b-d5911a238781 | -11.08057 | -55.05476 | 2025-06-18 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8735cef3-1482-3461-8c52-c228dd723639 | -7.08292 | -44.38533 | 2025-06-18 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53080576-b5cf-3017-aca3-13a251057555 | -5.90853 | -43.44984 | 2025-06-18 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c2cf7c1b-4f7d-395f-b6dc-a5f7d794b369 | -10.95333 | -49.25401 | 2025-06-18 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dab36fa-ca53-3cbb-93fa-b7f5d3537c39 | -9.41633 | -48.41756 | 2025-06-18 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9c82ce0-9e68-30d3-9fb6-f8abff7f0798 | -9.32714 | -47.83158 | 2025-06-18 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 361be247-6d96-3c75-8198-7b34e87790e0 | -9.27264 | -49.6159 | 2025-06-18 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8661bfce-a6f7-3ee9-82af-ac5f200fc955 | -11.64788 | -54.14028 | 2025-06-18 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9525368d-e26d-385b-bdf4-c42376f0870b | -7.81179 | -46.57344 | 2025-06-18 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5f31aab-c67a-3db0-bfee-941f288c6b84 | -16.31609 | -58.25577 | 2025-06-18 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8f84a802-8008-3b7d-a29b-d7bbf5703f8c | -7.14783 | -43.29362 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc2c7ecf-e78b-39ba-b72d-86ad02e22d17 | -5.60967 | -45.97852 | 2025-06-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e902ec1-e294-304c-aa59-f0f2a78e11bd | -6.23896 | -43.37009 | 2025-06-18 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd5a118-ef8a-3cb1-b38c-903c9632bdce | -10.87712 | -49.54922 | 2025-06-18 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad546301-3f23-36f4-8b8b-fb14015c5b74 | -6.41531 | -43.55875 | 2025-06-18 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8838fe53-b9cc-35f0-b993-a0b4b3bb9108 | -8.72308 | -49.0173 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd99a087-33b8-3de1-a926-65441751a4ac | -11.66077 | -44.61615 | 2025-06-18 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a50b96e6-b76a-384a-8578-240dde4088f7 | -8.72657 | -47.99411 | 2025-06-18 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b829455-c7b9-3d94-8eb5-9a26d5f768f8 | -9.84093 | -44.70105 | 2025-06-18 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70eaf8f2-6de6-3bd6-a9ad-e571fc94e8e4 | -6.36332 | -43.6571 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02476415-27aa-3324-bc75-d08f82704319 | -8.72271 | -47.99344 | 2025-06-18 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec5417c8-a595-37f0-a84a-44aeae7b888f | -7.48598 | -49.57702 | 2025-06-18 04:17:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fce78547-a3a5-3e86-a983-24ba9df65c76 | -6.12907 | -42.54172 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 562917d2-0bc3-353a-b39c-7b5d3f7b28b1 | -6.11742 | -45.93793 | 2025-06-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb2d76b-6a47-3285-8f6c-654c55452564 | -9.41326 | -48.41191 | 2025-06-18 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be01dec7-bd53-3ccc-9751-5b33cf6afca0 | -10.91873 | -56.84462 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 434855f8-b8ac-3ed9-bcad-22eb5dfb7e61 | -6.65694 | -43.19117 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a1d06870-a33e-3d63-a319-c3f0c36ea435 | -11.07971 | -55.05907 | 2025-06-18 04:17:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ee9aec9-fa5b-3a0b-b2f2-7cd71842e929 | -17.50692 | -45.26889 | 2025-06-18 04:17:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| afca104e-5352-3bf9-bf58-c10327c0df99 | -8.6735 | -51.4686 | 2025-06-18 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f9bcfca-e4ce-34c0-a3e8-d0755278b04c | -9.88255 | -44.79474 | 2025-06-18 04:17:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 654bf151-d8f6-3dc8-ab88-2fce82c743ba | -7.0006 | -44.07114 | 2025-06-18 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9adc5ee-9fad-3aa9-b12f-1a00246fcf1f | -10.61916 | -54.91977 | 2025-06-18 04:17:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68e880fd-e0dc-3120-a377-d4a7cefbf726 | -9.81799 | -48.1066 | 2025-06-18 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afd49f11-298e-3a97-a681-411c2dc90862 | -5.61393 | -45.97501 | 2025-06-18 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 763a7dae-853f-3561-8ef0-794de928659d | -8.10855 | -45.54571 | 2025-06-18 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 874d54e5-97b0-317c-85f8-1edcb2f0a3db | -12.13652 | -47.42282 | 2025-06-18 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51945ae4-a0c6-34ba-8385-ed2a842ec22c | -7.23494 | -43.10443 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1bb97578-8e49-3787-8529-a284cd7fc41d | -11.64857 | -54.1367 | 2025-06-18 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3faeff-3dd4-3973-8212-24947d5a4480 | -12.05141 | -46.979 | 2025-06-18 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 139d6b07-9192-324e-818a-5e77e38f0813 | -9.26344 | -46.56306 | 2025-06-18 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7192d978-daad-3a1c-bafc-fb934ccb28a7 | -18.37893 | -44.50959 | 2025-06-18 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 815abd76-6445-39de-9ff5-c23b476d7d05 | -6.12629 | -42.5377 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 682d7ceb-c418-3f37-8c98-2e9a4e54d9f5 | -6.63757 | -44.52704 | 2025-06-18 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d211ecbb-a5ad-3cb1-97d1-c81a63477a87 | -17.09459 | -43.80332 | 2025-06-18 04:17:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3e4f9bd-14c8-3248-aaf4-d535c34a3f76 | -9.49389 | -56.08579 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 75ff8c77-2c19-3c47-9c67-8dfe3ed7b02d | -7.02341 | -43.54821 | 2025-06-18 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8720b5b-9c2a-3798-be7f-e9fb7d2bf7b1 | -10.98372 | -45.10957 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fa6dc91-3b9b-3acd-a6fd-d7c4685ce500 | -8.59995 | -48.05553 | 2025-06-18 04:17:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f081410-17db-34ad-a213-01801fbfc4c9 | -7.80886 | -46.56868 | 2025-06-18 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbfb68c4-3d82-325b-a5e1-27c709d581e2 | -9.1571 | -49.64188 | 2025-06-18 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7cc1547-cf20-334f-9ecb-6b48ffb1dd22 | -10.88058 | -49.55376 | 2025-06-18 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 137a4819-2c0d-321a-b0c5-c12d289d1b0c | -6.37428 | -43.75228 | 2025-06-18 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1fe4b931-a5ff-37dc-9457-af5d06e7d64b | -7.21079 | -43.21459 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0549ad3-01b0-39d4-85f6-02bf30f63dcc | -9.26043 | -50.03644 | 2025-06-18 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2140ff2b-d9de-367a-aa3b-cb003052d2be | -6.11956 | -42.51522 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 01e8f74c-752f-3c10-a3b8-6f83c6d40fe1 | -8.06528 | -43.11773 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 41d64a58-e0a6-3016-89c6-bddbc94f5c8a | -7.28121 | -49.99975 | 2025-06-18 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a050d4be-c41b-3772-ac9d-cc4f3702039c | -6.66325 | -43.1885 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ab7f3553-97a6-3bf8-8f2a-cbc413edfded | -6.11962 | -42.53666 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 175081b1-800b-362e-a943-2a20b397cd0d | -10.34719 | -44.30591 | 2025-06-18 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0408cfbe-61b9-3718-9496-194dd1af1047 | -8.72492 | -48.00381 | 2025-06-18 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 308bb11c-2755-3c34-9420-61728a45f165 | -10.98429 | -45.10598 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cb9846f-c2bb-3bcc-a205-b9ff804eeb50 | -8.33668 | -47.07625 | 2025-06-18 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bca689c7-34be-3987-84fb-3147e33b194f | -6.12071 | -42.52968 | 2025-06-18 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 452db612-ce3d-33df-ac16-4b295ce8b8f8 | -8.72534 | -49.02909 | 2025-06-18 04:17:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83c357f1-407d-3421-af16-2b00a5d8ef18 | -8.59911 | -48.06044 | 2025-06-18 04:17:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8543cab-66e4-3b43-90bb-b16704bd88f6 | -6.67377 | -43.1866 | 2025-06-18 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c4984261-3841-37c7-86df-9073f6c7e78e | -8.13411 | -47.98947 | 2025-06-18 04:17:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40fbeeb2-79bf-360c-90ba-30a41d7f738d | -9.48637 | -56.0883 | 2025-06-18 04:17:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4e6320e3-e24d-32f2-9891-6097a9783ca9 | -11.33805 | -45.2148 | 2025-06-18 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b35fbefb-2c5c-3580-87fb-5cdbb109b58e | -7.23604 | -43.09747 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e7e62ee3-118c-3a4c-8873-81e7a9911208 | -9.46211 | -57.85626 | 2025-06-18 04:17:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 876d4cc9-6ce7-3150-85b8-5bf8c2dc7ac5 | -7.43661 | -44.90325 | 2025-06-18 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc56ab0e-de5c-3e4a-8e41-831509906a00 | -7.03457 | -43.2188 | 2025-06-18 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 55fe626b-c7a7-35b6-96cd-7557e68c0f06 | -8.06915 | -43.11477 | 2025-06-18 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8ef7eae5-27d5-32d3-815c-82341922f9e0 | -16.31717 | -58.25449 | 2025-06-18 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fcc84c35-20d7-39a6-8bc0-33fb1812ee04 | -11.14384 | -53.93 | 2025-06-18 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d70cad76-db77-3ac6-a04f-e5b8609a5639 | -18.37949 | -44.50582 | 2025-06-18 04:17:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13832a30-f192-340d-a5c7-7b0133193651 | -6.04012 | -44.04845 | 2025-06-18 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 96be6517-d630-3175-bbf2-804f5405b92e | -9.81719 | -48.11132 | 2025-06-18 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49657569-d8d6-3300-8029-a409b36316c2 | -10.92116 | -56.84508 | 2025-06-18 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e09316f-fd3d-3720-8b42-a81aa88c7245 | -6.41888 | -44.801 | 2025-06-18 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdd837b2-a6a9-38f8-9ed6-090ce4f7d771 | -14.20108 | -45.51156 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 886de7e1-ac75-39c0-b99b-d9b98bf515fe | -12.53948 | -57.72404 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc5f11c-bb4a-3de9-bd67-a65fef4cd11c | -22.78203 | -49.31796 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bae3c134-ca4e-3359-94eb-41391ef0a930 | -14.43925 | -48.90941 | 2025-06-18 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f2bb1609-b5a5-3144-adfa-8449c40cb212 | -21.37424 | -48.95935 | 2025-06-18 04:19:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c12420d-9be7-3721-98d9-0bb2597f4e73 | -20.42197 | -45.58433 | 2025-06-18 04:19:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 261cb31d-1788-36db-bf0c-91b628853185 | -22.78623 | -43.75631 | 2025-06-18 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 24847b95-0f3a-37f1-bfbb-bc44d904fa85 | -11.96084 | -58.7247 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac89da7a-5819-30d9-b9cb-b0c1ca66250e | -15.62531 | -46.46317 | 2025-06-18 04:19:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc4a2ddb-3237-3154-9c2b-d3837530010f | -14.20383 | -45.5157 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e4da9a0-5eba-3872-a635-6f3a4d8d4927 | -14.02985 | -55.12173 | 2025-06-18 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| baa438e8-7f8d-39fa-bb23-54298783e2e9 | -12.64408 | -54.11931 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51b36bd2-048d-3212-8091-d1d2de3ef8b3 | -22.67531 | -42.85301 | 2025-06-18 04:19:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| a0c6bc00-2e60-38f6-a08e-254b65e66857 | -22.77512 | -49.31654 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cfdda5a-1991-3352-aaf1-e486c65a4d59 | -12.64941 | -54.12917 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3a26aafa-850c-3499-a6eb-4f569fcd5947 | -19.58725 | -53.50262 | 2025-06-18 04:19:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)

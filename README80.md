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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd7e929f-cb2e-3e04-8b29-6fd92ec94199 | -3.89387 | -50.07461 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a92bee8-0511-363f-8199-788335d1cddb | -4.10953 | -49.50447 | 2024-11-24 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca63587e-db05-39bb-82a6-acfef28579d9 | -4.38219 | -55.08229 | 2024-11-24 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b20920c3-4bb0-34c8-9b14-abe7adc222f5 | -4.84919 | -50.80634 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c34dcd8-2a8e-3a38-b571-6936ecdc1849 | -3.51891 | -53.82242 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96d34bff-ca9a-3255-8c3e-7ee6bb34d7c9 | -3.70749 | -51.7971 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7340391c-5a74-35cf-a72c-c782a5676fd2 | -4.05683 | -53.64577 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 991bce87-736c-3882-9657-e11d8922f402 | -4.38411 | -55.06979 | 2024-11-24 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4cea358-5f02-38d2-8d5e-6107fb31b82f | -3.51187 | -53.81652 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 64b76593-e4da-3881-add4-0897347924aa | -4.50556 | -55.82788 | 2024-11-24 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 590d5ae5-9be8-3797-a3eb-9a7a63cb9ea8 | -3.2483 | -54.25124 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f019e677-72ca-3a17-a0c0-e32892074b29 | -3.50869 | -53.81129 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82a38d24-a0a7-383d-b7a1-ad1ec2cbd14d | -4.15787 | -54.57834 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0f2911cf-d616-3ede-8487-aaf58560d420 | -4.26644 | -48.69014 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce196967-786e-3349-aeb8-f1996d2915b3 | -3.25417 | -54.23837 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08847b1f-8604-3a5e-97f6-b26b4d0c7399 | -7.57241 | -49.40357 | 2024-11-24 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ee7507a-cc71-31ec-9169-a73757b3bbef | -4.36813 | -48.56312 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2df42e95-5ee1-3af9-81d0-681a2a339f73 | -3.25346 | -54.24289 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 102aa146-0d60-34f4-ab60-f48fce3171c5 | -3.15626 | -54.96047 | 2024-11-24 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d66f168-9489-3a64-a13e-2fc6013eb33e | -3.18665 | -54.76706 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59190dfc-6572-3ea0-8338-05b7785102dd | -4.40753 | -49.65689 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8afeefd0-8da8-330d-bf2b-86b11d1036ad | -4.11525 | -49.50206 | 2024-11-24 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90eb2e80-e708-3f4f-ad1a-4004e07acbd2 | -3.29359 | -54.72483 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42905a0b-9f3e-3bf8-b54b-63d8a1be30a5 | -3.51161 | -54.7368 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 101fed44-6e58-3272-a54b-56dc675a52f0 | -3.79111 | -51.92728 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd8167a1-494d-37f5-96ff-142ae3f55826 | -7.57745 | -49.40818 | 2024-11-24 05:16:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 267e2216-af97-3bfe-a145-b8dee2884a67 | -3.49642 | -54.01896 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3abb8b0-d72e-342e-b7e5-d34453ae4669 | -3.51724 | -53.80741 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1069eefc-4ada-3e89-b6d3-114316ba5f76 | -3.15317 | -54.95828 | 2024-11-24 05:16:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9500704-0d4f-3b4f-9157-8e80054c2e52 | -3.18233 | -54.77072 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34c0ab41-873b-3944-92cf-99bf34772d57 | -4.37802 | -49.75156 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 043f36dc-45f4-3b1b-859d-48535aecfdb9 | -4.3789 | -49.74535 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7323db93-1236-3a6e-906b-0bc9651b3ffa | -5.57014 | -50.94845 | 2024-11-24 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3b55fbb-0394-3a2e-84f5-add0a9627eac | -3.81091 | -52.00471 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5767af23-8c8a-32ea-b898-0cf57bb2756c | -5.95279 | -48.0477 | 2024-11-24 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fdcf749-3dc9-37db-a453-9fb9317c855d | -4.23547 | -48.70796 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb6b9a6f-25b2-3ed7-bd2a-703e421fd559 | -4.84679 | -50.80492 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9673e12e-3b74-36f5-aa4a-5710d79e8923 | -3.25111 | -54.2332 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6792e94-8e8e-306d-b04c-0b6bfb8bf899 | -3.66738 | -51.57267 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e718ee8-c9fd-3c0b-8a75-821c112e79a7 | -4.52733 | -46.42542 | 2024-11-24 05:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e15e6666-83ae-33ec-b524-a4bc14d933a7 | -3.98751 | -49.92973 | 2024-11-24 05:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4560223e-576a-3163-936c-246ebe5314fd | -3.78364 | -52.29756 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09af8003-a254-3c52-aea5-b9ea68254f1f | -3.24876 | -54.22349 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0eaf4c76-de3c-3866-8880-0c022fd92582 | -4.34383 | -55.77594 | 2024-11-24 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 32e85f6c-f5ef-3d09-969d-bc45ca359ebb | -3.17591 | -57.04046 | 2024-11-24 05:16:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a163c0b3-001e-32cb-aa73-655ec6927bb1 | -5.95217 | -48.05217 | 2024-11-24 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19eeef49-f640-3b42-b305-a537a2dfca33 | -3.50626 | -53.80123 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66895f32-7414-34ad-ab49-a981f21ed28d | -3.25488 | -54.23379 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d329e4b2-fd79-34e7-ad48-a1e8a4bac78c | -4.88553 | -48.90792 | 2024-11-24 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21c666b8-9707-3c13-810c-8627bdf232e1 | -3.7499 | -54.7815 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee55904-971a-3513-bba6-b2f1eb568f41 | -3.52266 | -53.50862 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a9445a0-fbde-362b-90eb-475f3d1d2bf3 | -4.05609 | -53.65071 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce2e39a7-dc97-3aff-bc05-7ead77518c03 | -4.26089 | -48.68926 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbef24bb-30bc-3688-944b-6faa8c13a495 | -4.03428 | -51.02016 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a553cc-fa18-303e-8675-8d9dd8b2a84a | -4.48606 | -48.11341 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a47bf49d-1e60-33b3-a7d7-ebb030ee0649 | -3.7736 | -52.40583 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8ecd1c08-9af9-366d-9bdb-ab324f9ca7c3 | -3.49185 | -54.02314 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c5ef1ba-ed7e-34a3-b0d2-4374cc75dd07 | -3.53878 | -53.07204 | 2024-11-24 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b67429f-6b1f-3e59-85ee-1124977af04e | -3.507 | -53.79639 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea88a550-fd8b-345f-a36d-0c42cfe43d45 | -3.18846 | -54.77405 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5d3950-c3bc-3caa-80b8-a108b385d637 | -3.25465 | -54.21048 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87719221-a535-3d05-bf5f-af78f83b1025 | -4.63646 | -48.84355 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e31e8e3f-e39b-3d50-9297-605ebb99db65 | -3.31862 | -54.09053 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 035d97cf-deb6-3b47-8a10-e80e0e041108 | -3.18533 | -54.77546 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb7208e1-3a68-3919-96bb-274eb0197d2d | -4.26591 | -48.69382 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52ac4072-76ab-3ed1-96af-65d62ca2e576 | -3.51016 | -53.80172 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37eda4df-2804-30a2-a5b7-88fd44bd4046 | -3.80478 | -51.33947 | 2024-11-24 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f701018b-667a-36e2-8816-2bd03d94a454 | -3.63793 | -52.25645 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e2b0640-8647-3117-b3ef-e06053775814 | -3.61087 | -54.74643 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 627b34c4-e75a-3ffd-85be-3204abab3bac | -3.85082 | -50.43315 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e765b3b8-be92-3144-811c-6c582e369302 | -3.95251 | -50.19905 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a7e3c0c4-ede0-3291-bcdb-8c92626ab9ce | -4.51133 | -45.72443 | 2024-11-24 05:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f239929-5570-38f4-a03e-e534b94e7f29 | -4.24055 | -48.6331 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cbcee564-d14e-3ee5-8e08-ae326fe2a432 | -3.9575 | -50.19989 | 2024-11-24 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| badaf6aa-efdf-3fa5-bcc6-414233e9302a | -3.63855 | -52.25238 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a0a5968-227f-3869-937a-2357c0499f4f | -4.52588 | -46.43028 | 2024-11-24 05:16:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937891c8-7e67-3a92-b190-11e87442d439 | -3.52429 | -53.8133 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d63beed-a484-3c3c-b985-6db8e2f9d665 | -5.95156 | -48.05653 | 2024-11-24 05:16:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 764c21b9-6143-3062-af47-bd27cff3aef4 | -3.8161 | -51.99463 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16ad37e9-cbea-3264-b049-d350760ddfcf | -3.57781 | -54.51762 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bb190e4-1935-39ce-af05-5705365ff911 | -3.51965 | -53.81759 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bbf4924-ee52-3fc8-bf4b-d518d59cabd2 | -3.50796 | -53.81608 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 29f36866-852d-3d35-b0b0-d79a3605030c | -4.25425 | -48.69587 | 2024-11-24 05:16:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7e2a39c-16b5-3f33-9213-a344a0e0fb86 | -3.42415 | -53.28228 | 2024-11-24 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70410cc-1da4-3ce8-9df8-7c9dbd97a988 | -3.67534 | -54.5847 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d30b6be-3b30-3207-bf6d-277272f31319 | -3.249 | -54.24675 | 2024-11-24 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d60a04aa-5b0f-3e11-ad9c-a83de16fff13 | -3.67072 | -51.73783 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b2b8f72-61b9-3b82-bda2-1c6e423cf930 | -3.18177 | -54.76874 | 2024-11-24 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7656b51-24e0-3e9b-b880-92d293f8c59f | -3.31792 | -54.09514 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 553aca84-e1a6-3cd4-a5b2-18868391b627 | -3.50552 | -53.80605 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f05faa6-a3bd-3af1-a4da-9ac8b680cad3 | -3.80941 | -51.34003 | 2024-11-24 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 338bbfc8-4a2c-381e-b947-a8c1ee24d7db | -4.05977 | -54.6147 | 2024-11-24 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6febb679-f636-3213-b3c9-5c5ee79ec5f4 | -4.11356 | -49.43927 | 2024-11-24 05:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a07452df-ac32-38b5-a47f-2b93f8c65d6f | -4.21335 | -50.40295 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f043f40d-ec27-3068-884e-301502ce94d2 | -3.32244 | -54.09103 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e78fdc0f-3bec-3505-b5e1-b5e26422f571 | -3.77786 | -52.40661 | 2024-11-24 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 67e540a4-157a-3c1d-b220-b74dbf7d8c52 | -3.81663 | -51.99675 | 2024-11-24 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eef29bc8-f7fb-328b-aaca-79a222230f1e | -3.5165 | -53.81223 | 2024-11-24 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d2b66da-2273-37e6-bd58-9c4708a32856 | -4.08634 | -50.36433 | 2024-11-24 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de0c3cb8-11f0-375b-b90c-dda18f9f7f6b | -4.63547 | -46.86756 | 2024-11-24 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README81.md)

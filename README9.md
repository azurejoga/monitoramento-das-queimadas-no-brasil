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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d845c7a2-23da-342f-852f-746742bcf39c | -8.71444 | -48.33718 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 085de922-518c-3c0e-b7b3-3d058a657343 | -9.20229 | -45.31937 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a246487d-2b68-386e-92f1-b8859a1dd93d | -12.52063 | -48.28947 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f83335ad-f5be-3060-b670-810f216e33e6 | -12.85697 | -44.35524 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 40973946-0ed4-3fec-a17a-0b7f646ba543 | -10.69689 | -49.60831 | 2026-07-02 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 375495b9-8f35-38cc-bfe2-305bdd1ffa81 | -9.53126 | -47.75577 | 2026-07-02 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34e196eb-0c98-383f-ad52-5123fde2254a | -10.37296 | -46.68324 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d02ab1e1-2ce7-3494-9f28-dda4b8bd666c | -10.8431 | -45.06116 | 2026-07-02 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20789171-6c05-3b8f-ad13-e774982a30a8 | -11.85754 | -48.24619 | 2026-07-02 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bda084dc-4b12-3cf7-9b4c-205097f86b64 | -12.85263 | -44.40446 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c3af3e8-c2b8-311e-836c-a85893fe072f | -12.85321 | -44.34898 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| e52c1ed2-9da6-34c9-a390-737ffeaa8654 | -9.16239 | -47.23477 | 2026-07-02 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce5db89e-41f1-3aba-8712-cf8791385aad | -10.37377 | -46.679 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a71db802-fa59-3205-b194-671b1efd3cd7 | -11.86788 | -45.60807 | 2026-07-02 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fda2cfe-a235-3519-b599-800177b93066 | -12.7865 | -44.49619 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 5bd5da3b-7124-36bf-af81-d23ce69663f6 | -11.85135 | -48.24474 | 2026-07-02 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5e7c961f-eccc-388e-878e-9443bc948e4f | -12.79249 | -44.51074 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8fbbe211-9411-33ac-8b1b-42a1ee4f9653 | -12.51704 | -48.28144 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 93f133a2-2e5e-3bfe-97d2-c7f85c7f7199 | -9.50183 | -40.35382 | 2026-07-02 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ade493b6-8011-3522-860a-9e96ebd96402 | -8.32057 | -45.37695 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4432591f-8c63-3a71-ac38-cc6f228baac4 | -12.78167 | -44.49526 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2f927722-34e4-31f2-8117-561320a92288 | -12.79413 | -44.50908 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6e2c867d-36dd-3687-aa3c-7048ee102779 | -12.84641 | -44.35874 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 6e9b16a9-f625-304f-b909-5aaa5ee7a798 | -9.16146 | -47.23954 | 2026-07-02 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23568c4a-62de-3f44-a258-d9f720aeb740 | -11.85236 | -48.23964 | 2026-07-02 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bcf86193-7a22-3d87-8562-7c3996e05594 | -9.15533 | -47.23838 | 2026-07-02 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57c38130-3b71-3741-9ae1-8bb7a734b67a | -11.00066 | -47.18765 | 2026-07-02 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0731ae1a-d51e-3d47-808d-ffec149bcecb | -13.29461 | -43.55436 | 2026-07-02 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89f9e83f-e9c9-3520-bd18-d4e93ac14fa8 | -10.84489 | -45.05624 | 2026-07-02 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebeec058-0b8f-3442-baa0-7b88fe656e26 | -9.19077 | -45.32082 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b08d7d5a-4681-364c-b69b-1415b74ef3af | -10.94973 | -43.05643 | 2026-07-02 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c15564f3-6125-321f-8f33-78abea773fa7 | -12.51087 | -48.28019 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b15b9b75-2c79-371a-9f6e-0f31ef1fbdda | -12.50988 | -48.28517 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3f0276b-a6fe-3552-a394-0a67f3bd84c1 | -12.75754 | -44.49057 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| cb5e4a27-d411-3d0e-9d8c-86d4d8058596 | -8.71998 | -48.344 | 2026-07-02 03:45:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c73e78cf-36a4-372a-9716-6effc1f9e68e | -9.75537 | -47.87941 | 2026-07-02 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a265d95a-a675-344c-9727-3bf9e95eb4e2 | -12.75096 | -44.47231 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af6cc481-b1b1-3820-b813-22b5a86f43d5 | -12.84988 | -44.39277 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 57d3bf62-9e6c-38fd-87ea-e979a00171a0 | -12.76339 | -44.48603 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3b6ef45b-cecf-3bb6-a890-7239b9655351 | -12.51446 | -48.2882 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 33df3f8f-8d1d-3259-9adb-b9cd537b0451 | -10.37215 | -46.68743 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7328cbf4-8a9f-3b73-ae11-aae3863fb698 | -11.855 | -48.24778 | 2026-07-02 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4752ac2c-8a4c-3000-8d23-abf8981bd292 | -12.84843 | -44.34808 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 743bd448-3629-3f03-84ff-80633903f6a3 | -12.84944 | -44.34275 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ecdd293e-c7b1-3da8-848e-1179e3cac9d5 | -10.8055 | -48.56398 | 2026-07-02 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0176b84-b97d-3781-8867-400854278431 | -11.91647 | -43.38596 | 2026-07-02 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86c7d05e-3685-3654-a261-6138b3ed5c43 | -9.74187 | -49.02889 | 2026-07-02 03:45:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a270e3f-4c1d-3ea9-9ea7-8e4d5aa4c0f8 | -9.1555 | -47.24044 | 2026-07-02 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b927285-8fda-3357-b156-9705aebe6c73 | -12.75271 | -44.48965 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 93e08f09-7a8f-3d9b-b9dc-9be5723d19e2 | -10.84886 | -45.05901 | 2026-07-02 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62acf24d-3843-3f49-85dc-6c871e590521 | -12.5165 | -48.27829 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29297eeb-6643-31fc-a7ab-74c8a58978ba | -9.75846 | -47.87865 | 2026-07-02 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd52c1ff-3c9d-38b5-88f3-25d1ea2532d9 | -12.85898 | -44.3446 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b0b2ea4a-0012-33b5-9727-46602448eba0 | -10.38123 | -46.67153 | 2026-07-02 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 508b4af4-87bf-3a5a-8168-afea5bc1da14 | -11.91103 | -43.38985 | 2026-07-02 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91328fd3-f6e3-3bb0-b282-f3a0b0762fa3 | -12.51032 | -48.2771 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b1a884e-c10a-3919-82af-6620e966588b | -17.71824 | -46.79037 | 2026-07-02 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72cd702d-45e8-3e4e-9844-a17f31f68660 | -20.48024 | -50.5248 | 2026-07-02 03:47:00 | NOAA-21 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9eb4b8ed-7953-3109-a3bb-0e225236abf0 | -16.43833 | -43.48923 | 2026-07-02 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6144d9a-9b18-3553-b2b7-6dc0a5560f0b | -19.17103 | -47.35632 | 2026-07-02 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b367d61-a9a8-3415-9af3-f3de9f9127a5 | -19.17615 | -47.35762 | 2026-07-02 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03806431-9109-3037-a001-042c907b9114 | -14.81505 | -49.00972 | 2026-07-02 03:47:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 70c46530-289a-3d36-b203-bb65e325d518 | -20.58815 | -40.80333 | 2026-07-02 03:47:00 | NOAA-21 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27d35f28-70e8-3633-92cb-f28d4995ce63 | -17.71376 | -46.78617 | 2026-07-02 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d3b509e-0695-3022-871c-878a2c3f3d0c | -20.48611 | -50.52617 | 2026-07-02 03:47:00 | NOAA-21 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7c6768bf-8520-3516-be03-2cf64b7cdcb4 | -19.49851 | -52.73009 | 2026-07-02 03:47:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2c8eb69-a892-302f-b9b6-a45c680e5db3 | -19.17682 | -47.35443 | 2026-07-02 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cceaad7-69cd-3082-b048-1588472eed6f | -21.49548 | -48.5412 | 2026-07-02 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b555a742-5d95-3820-b8a1-a1c01546374a | -19.50539 | -52.73215 | 2026-07-02 03:47:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 664ef480-0272-3a12-947b-852009f027a1 | -19.51049 | -52.74138 | 2026-07-02 03:47:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f217f93-708e-37ac-8ff7-d87b8adc9a5d | -17.54576 | -49.42671 | 2026-07-02 03:47:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38973e25-627a-3bbf-892c-564fb7f825bc | -20.24125 | -40.37963 | 2026-07-02 03:47:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2275b83-99be-3021-8e6e-a5a1fa7fa2cb | -19.50034 | -52.73105 | 2026-07-02 03:47:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d4fa626-7e39-3c3d-af93-cb26b0138af3 | -20.48632 | -50.5262 | 2026-07-02 03:47:00 | NOAA-21 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d06fabdf-29c6-3a94-8e94-ab2ef6f151fd | -20.70505 | -50.52143 | 2026-07-02 03:47:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 14327cc0-897b-342c-b195-fc26ccbc300b | -20.97434 | -49.10169 | 2026-07-02 03:47:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a122616d-68c3-3d3f-9161-5c6393e37702 | -14.81334 | -49.00982 | 2026-07-02 03:47:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caa107c2-b02f-3704-b9df-82cc27512c6f | -17.71309 | -46.78946 | 2026-07-02 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6b05336-cffa-3bd8-b362-7da981c3ecce | -17.71756 | -46.79368 | 2026-07-02 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b081e4a8-0dd1-3448-be62-1b646ffa9001 | -20.73714 | -41.10159 | 2026-07-02 03:47:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 49dd3146-47ba-36f7-964e-a126cd897a5f | -18.13269 | -43.97395 | 2026-07-02 03:47:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c5790e4-9b79-3850-8264-211fced1b9f4 | -20.70396 | -50.52621 | 2026-07-02 03:47:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 285acea1-601a-3c57-8783-e8f7be9adeb3 | -20.70531 | -50.52363 | 2026-07-02 03:47:00 | NOAA-21 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 58545fe5-f6cb-3397-baad-7005f81960c9 | -16.39526 | -47.41831 | 2026-07-02 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4fcc849-09f4-3695-b6ec-be632fd1dfc0 | -20.48003 | -50.52473 | 2026-07-02 03:47:00 | NOAA-21 | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 16a6e75d-bc12-3c1b-9c6c-c7644388e244 | -20.31661 | -40.85344 | 2026-07-02 03:47:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7a507797-903f-36ed-8585-385a77aeac05 | -19.50549 | -52.74026 | 2026-07-02 03:47:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa1bc61e-d6f9-3254-9467-2a0a30fc6fa3 | -17.71891 | -46.78709 | 2026-07-02 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a8511d2-a82f-308a-848a-672afc03d2d7 | -21.45228 | -51.36392 | 2026-07-02 03:47:00 | NOAA-21 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 951a5e86-b088-380e-922c-67627520873a | -22.79542 | -49.34859 | 2026-07-02 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0e31079-1fa1-31ad-9e1c-5c0e1f843c59 | -23.56255 | -47.50888 | 2026-07-02 03:49:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e6283b8e-ac82-32b4-a52c-65c003965602 | -23.56649 | -47.5114 | 2026-07-02 03:49:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 57683240-6c16-3197-9015-75f33dcc1046 | -21.80266 | -52.72346 | 2026-07-02 03:49:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99c15425-a3e5-33e6-b879-36412f5284a9 | -21.80418 | -52.71745 | 2026-07-02 03:49:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0e5a275-f1cf-30c0-83fd-35c49acdc29e | -23.56171 | -47.51035 | 2026-07-02 03:49:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 10f24920-85aa-3858-8c20-aa481b86f36d | -22.79453 | -49.35255 | 2026-07-02 03:49:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93392eac-dc54-3982-947d-ff011f3e1dcf | -21.7823 | -56.2976 | 2026-07-02 03:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 873e5c44-13fa-35b7-b6a7-c531c3539c61 | -11.4149 | -56.0525 | 2026-07-02 03:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0ab65d81-4c76-3546-924a-f3567d99f5ff | -12.8557 | -44.3154 | 2026-07-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 5e160f54-f051-3621-bde1-1cf4793d15e5 | -12.8552 | -44.3389 | 2026-07-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 426.3 |


[Clique aqui para ver as próximas entradas](README10.md)

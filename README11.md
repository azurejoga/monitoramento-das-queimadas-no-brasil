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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8a4deff-de17-3690-ac6f-cf62de189454 | -3.89357 | -47.08468 | 2024-11-02 00:54:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8603e8d6-f87c-35b2-8b00-f81f72462164 | -3.8784 | -46.44782 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4e56e7cc-c67e-3f03-8e1e-eb40bf6bdbb8 | -3.81757 | -46.48629 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5749d85b-9775-3545-8a32-8a4bcfec06f7 | -3.63961 | -47.30792 | 2024-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d21d275d-452c-3462-95b8-47aeb4859092 | -3.63095 | -47.31539 | 2024-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1d00e976-ab3e-313e-8964-5fd8083a9fdd | -3.62968 | -47.30628 | 2024-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 81d27ce2-71cb-3c80-b7d5-3a6d09eb4bf6 | -3.62196 | -47.31668 | 2024-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cb0ec8a3-7bb7-3e60-8240-8a2406079efe | -3.62068 | -47.30758 | 2024-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 57f9783c-10fc-3d56-b1c8-174f737b88cb | -3.59371 | -47.31149 | 2024-11-02 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f91e674b-d8a3-37cf-9ed6-9fc3901e76bf | -4.97784 | -46.47204 | 2024-11-02 00:54:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 903d37c1-0089-3e73-9dd5-fc6cb25e0c6f | -4.96354 | -46.50333 | 2024-11-02 00:54:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4b79868b-7964-331d-861b-f0a71cbc966d | -4.8735 | -47.36642 | 2024-11-02 00:54:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| b5447506-a538-30e9-b08b-fceb20db70cb | -4.70658 | -46.44118 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8e8efcc5-f8b8-3088-b040-646edee88fe2 | -4.70523 | -46.43157 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 19de3307-ac67-3421-a2df-67a36dfde442 | -4.69862 | -46.78137 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dcdbcb28-496d-39f8-af61-d90846b0efa0 | -4.69736 | -46.44246 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 11acb66c-6fa1-3129-9bad-031ad191fa7a | -4.69601 | -46.43287 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1c4900ed-14ce-36ab-8c9c-1fe453e01270 | -4.68136 | -46.39566 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 6e9dedcc-266d-3a5f-ac6e-8440075ac345 | -4.68 | -46.38602 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 3916c6e5-843e-3497-a533-bafb1cddb4b9 | -4.67862 | -46.37624 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0979403f-55bf-328f-94ea-66b99e7a1577 | -4.67075 | -46.38729 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9a3bf39b-0a3c-3795-bfa2-3f4e3cd1021c | -4.6615 | -46.38852 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77155f8e-a0b5-3219-a417-589daa3a09a5 | -4.66111 | -46.31919 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ccba9cf8-12ec-324f-ad75-a672df3f0b94 | -4.66013 | -46.37891 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ea70cb0c-324b-3972-a84a-a5bcb56c12df | -4.65483 | -46.6049 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4c35e51f-f2c8-3ebf-afbf-d67b348e621d | -4.65349 | -46.59551 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3650458c-b867-378a-8347-1c1814a5d571 | -4.65183 | -46.32048 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d14713f0-7405-384e-b293-88e9885ec44c | -4.5833 | -46.55339 | 2024-11-02 00:54:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 960196d1-d9ff-3524-8f28-ebb4affc34a9 | -4.51973 | -46.48971 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1bac943a-fa75-3bd3-9cef-7b96741c1b30 | -4.06474 | -46.28125 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 274dc976-eed5-3510-a02e-aaf55d4ea3c1 | -4.06046 | -46.25143 | 2024-11-02 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 60595101-7ee8-3d97-8ed7-ce3c0771de56 | -6.38588 | -46.78571 | 2024-11-02 00:54:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ae44035-6f1c-381d-9893-c3d112ccab61 | -5.51028 | -47.17688 | 2024-11-02 00:54:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| e94537f7-31a9-3646-8e1a-76a5dc6b5326 | -5.50901 | -47.16787 | 2024-11-02 00:54:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 63a556da-8770-39cb-b463-c227ce493007 | -5.50008 | -47.16917 | 2024-11-02 00:54:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c6891774-5d62-3d6e-b949-95ad0ee25eeb | -5.43476 | -46.51066 | 2024-11-02 00:54:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a2b23de-6ba3-3aeb-83ff-9c44ee76e5cc | -5.43342 | -46.5012 | 2024-11-02 00:54:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 43635737-ba10-334d-ac7f-b157c6f651bc | -5.36643 | -46.68033 | 2024-11-02 00:54:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03a0d009-08d4-3318-8649-f1d2e247b15b | -5.21884 | -46.74551 | 2024-11-02 00:54:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 52c214bf-c9be-30d7-9478-a93aa6e9772e | -5.15073 | -47.70586 | 2024-11-02 00:54:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b1db7193-ec43-3571-a4b9-e075b78135a4 | -5.14949 | -47.69698 | 2024-11-02 00:54:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b239332c-2080-3c74-af1f-65844fa012ef | -5.06126 | -47.72473 | 2024-11-02 00:54:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bbf26e3a-f46e-33c4-9355-5c40759c2aa3 | -2.05609 | -47.9173 | 2024-11-02 00:54:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 78c041d1-0441-35d7-b484-7e1cbdaa1c23 | -2.02326 | -48.40849 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c935d91a-fdc9-3642-97c9-062f4aca0642 | -1.85776 | -48.01248 | 2024-11-02 00:54:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dfa6b6ed-bb0f-3f7a-af76-abf3137ca148 | -1.82212 | -48.01755 | 2024-11-02 00:54:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8bd25c36-3a2c-3398-aec3-3e76a8f103ab | -1.78021 | -47.84916 | 2024-11-02 00:54:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f0a7c94-6a44-3c60-9f70-998cc5516f38 | -1.77893 | -47.84012 | 2024-11-02 00:54:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35a659a2-a947-32ea-a166-486148077b31 | -1.67461 | -48.15086 | 2024-11-02 00:54:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 44ea79c6-45f3-3d77-b32c-9529279fbada | -1.65228 | -48.52127 | 2024-11-02 00:54:00 | TERRA_M-M | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3fad736b-ba88-3102-a08a-ac7281e8bfc6 | -1.41547 | -48.01389 | 2024-11-02 00:54:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 12a1fc62-2dcf-3038-804f-a1f3f04d46fa | -1.06317 | -48.26169 | 2024-11-02 00:54:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 71f43db4-5ccd-3940-9cd2-c52d9d3f3ee4 | -0.9733 | -47.81417 | 2024-11-02 00:54:00 | TERRA_M-M | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba635209-b955-3766-9af1-2ca982a73159 | -0.9643 | -47.81544 | 2024-11-02 00:54:00 | TERRA_M-M | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9006a9dd-4f1a-3ffc-beea-a4f909d37e5a | -2.07711 | -47.66827 | 2024-11-02 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f8080f2a-ca42-3ccc-bc7d-f4a61da3854a | -1.84392 | -47.45121 | 2024-11-02 00:54:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d789d5d1-b579-32bc-91be-d812eacc4734 | -1.56597 | -47.30903 | 2024-11-02 00:54:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ee65cb63-b2da-3de7-8107-1bf23bcf253a | -1.48943 | -47.21945 | 2024-11-02 00:54:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95e091d6-800f-3c47-9007-757f1b92a76b | -0.9474 | -47.56349 | 2024-11-02 00:54:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 902ed797-34de-3fa7-b9c9-ebf8e6d78174 | -0.9461 | -47.55416 | 2024-11-02 00:54:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| f55dbf00-9fdf-3479-b957-bb938d45baa4 | -0.93832 | -47.5648 | 2024-11-02 00:54:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 032b71bd-42c8-318c-9685-afdcb971e15d | -0.93701 | -47.55545 | 2024-11-02 00:54:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4cb2e7e4-93f6-3f2d-9e45-57351db2a29f | -2.37056 | -48.85253 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc793b30-9305-3bbd-b240-c3fd7a669666 | -2.35982 | -48.69537 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbf9def6-fe66-3bcb-87ef-85b239159c50 | -2.3586 | -48.68659 | 2024-11-02 00:54:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 894c3f10-e13c-37e2-a0a7-2d92a0751cee | -2.2408 | -48.84085 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3338f867-607f-3599-9011-1857736cb252 | -2.18931 | -48.79438 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a8906700-0cfb-3380-8ae5-44d7b93fd823 | -2.17401 | -48.82967 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb706109-fc44-34d4-9eef-327a9d5adfa5 | -2.17061 | -48.7406 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cc4ad435-0870-33a1-9dc5-0bcf73f78b35 | -2.16938 | -48.73182 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5d39bb1d-4c94-305a-a608-d1f3a316fae4 | -2.12646 | -48.74683 | 2024-11-02 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80b369ab-d420-39e0-9140-8828ffe17e4c | -3.10975 | -48.65715 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 95f8ff08-2a44-3a5f-9575-e5c46d88da4e | -3.06419 | -48.00729 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d3da41c0-c2a7-307a-a6d6-b19c91b46581 | -3.01331 | -48.83542 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6f01d06d-a023-317a-81e3-ec80ff5983cf | -2.9763 | -48.63442 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 003e4e25-99f4-3212-9b86-875e948f83ff | -2.95863 | -48.63691 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5306eb39-3987-3954-8086-1ca662db070e | -2.9441 | -48.06683 | 2024-11-02 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b428b2c8-e303-34de-9f1b-1ae6484638f0 | -2.91964 | -48.61554 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 04626413-92f3-3ea0-9772-2fee2cec8c50 | -2.91841 | -48.60675 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bed8a9c1-0810-34b1-b128-ecf8373fad65 | -2.91326 | -48.63436 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| d5485547-23da-355d-b742-159affa513b6 | -2.91203 | -48.62557 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e819a6d1-22f5-3b4e-86c9-d3c22f07f651 | -2.91146 | -48.76637 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4bd0a8ed-5701-3988-ba10-def06292d60d | -2.91081 | -48.61678 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 48048bcb-0d1e-3473-9b42-e424f0fefad8 | -2.90958 | -48.608 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97339a4c-0304-398e-bf22-991ba81c5175 | -2.90075 | -48.60925 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2dc48a0c-4f5d-302e-a619-3f125345118a | -2.89953 | -48.60046 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ffcadf6-882e-3089-9074-2325e2bdfb6f | -2.85977 | -48.45995 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c2e17789-ec83-3806-a73e-5a54ac78dfbe | -2.85094 | -48.46119 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c46de337-ba12-3939-a863-05ce250f6f8b | -2.84088 | -48.45365 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7f6b5428-5486-3700-9df9-6fc1193b824c | -2.83965 | -48.44485 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 82cc6574-558f-3d91-813c-9d6d5b69651d | -2.83081 | -48.4461 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1305507b-ef1c-3805-a292-8677a234a453 | -2.82959 | -48.4373 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 945e2ff1-a552-3e56-bbbb-ffd1953895bc | -2.82737 | -48.35681 | 2024-11-02 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5bcfc2f6-511e-312a-9acb-c612d312e9e0 | -2.80358 | -48.65309 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a2f2d2cf-a5aa-3122-b8fb-fca94d030938 | -2.79379 | -48.58278 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 12e75d3e-958b-34b6-b23f-90ea16e0dfb1 | -2.78496 | -48.58403 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b60514e0-6872-3972-92ec-975bfc21e93b | -2.78373 | -48.57524 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| da7d4eb5-cffa-3457-9921-8e291025e0b2 | -2.77682 | -48.71959 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8bb10a4a-bf99-319e-8765-fcb83275e714 | -2.77612 | -48.58528 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 7657116c-a67c-3ef5-af42-6816561944a5 | -2.77586 | -48.64804 | 2024-11-02 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README12.md)

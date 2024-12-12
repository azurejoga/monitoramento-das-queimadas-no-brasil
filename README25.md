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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85d0d488-339c-38d5-b211-d1f64247723d | -9.3818 | -57.55264 | 2024-12-12 04:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afc2e708-bb70-3044-91dc-a8c06eeb6593 | -11.19763 | -53.82183 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d5ca960-17a5-3d2a-8157-536491add26e | -11.11941 | -54.64829 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d56d9470-8b05-364e-8682-b48493f21e7f | -9.23641 | -46.66748 | 2024-12-12 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f6e8f08-e11e-3a8d-a0dd-df47e48dc1ce | -11.69279 | -48.07805 | 2024-12-12 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdf6a060-b01b-37dd-bd6e-1f2e9ad74a3a | -13.69669 | -54.7677 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3466d16a-d6f0-3b91-8f21-7207cdeb6eaf | -11.84867 | -56.86636 | 2024-12-12 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a9ec66a-df15-36e9-b672-91c181a4e7e9 | -11.70812 | -57.35225 | 2024-12-12 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d8544b7-40d4-33f3-922e-947ae86a4aa8 | -14.74401 | -52.64862 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9401354f-7e61-3b17-8bd5-10979a0cf2a1 | -12.55045 | -58.35202 | 2024-12-12 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da82862f-cb6b-3317-98c0-3e3a25b37652 | -9.11315 | -49.46476 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48a462e7-4f82-3c10-9d39-d067b9b9b9b2 | -10.29163 | -53.70052 | 2024-12-12 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5a5726a-a173-30dc-891e-6d1549a51ad7 | -10.35086 | -57.24618 | 2024-12-12 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27a0a13b-cacb-3f76-9cb1-109ab82b68cb | -10.19306 | -36.22344 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 35d841a9-55a1-37a1-bddd-8d8974ded79c | -10.85254 | -55.16866 | 2024-12-12 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9b7cf5c-cbd4-3f58-8e49-bd89f8ba93c2 | -12.918 | -55.72471 | 2024-12-12 04:40:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9d7e2ad-e0c3-3ec2-b1b2-149df85169ab | -12.92427 | -55.04529 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0133e5db-c878-3b21-aef7-165d91659d03 | -9.1929 | -49.47354 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfd9084b-7dd1-33dc-80ed-00dd7ed60e66 | -11.20853 | -53.82365 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 015d1e09-59ab-3ad4-a20f-c1137c7f7263 | -14.74521 | -52.64127 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e44665e1-e7b9-3f7e-89ae-65f01aeff3cd | -11.88872 | -54.67611 | 2024-12-12 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 519f2064-2561-3c89-8e67-00722aefec2f | -10.49554 | -44.63829 | 2024-12-12 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c26eba64-a279-3b1c-9e04-42d072611d4f | -11.42545 | -55.91597 | 2024-12-12 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46ddcc9a-d415-3c12-8b2a-34369cce4634 | -11.20348 | -53.83152 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7bf2f337-1d2f-3efb-8699-732b5f552d73 | -11.78142 | -55.13103 | 2024-12-12 04:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5b19fae-c450-3a04-8eb1-e2570b734ac2 | -11.71051 | -57.35075 | 2024-12-12 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efdc4c5e-bdcf-3282-880b-c094e015a6fa | -10.29203 | -53.7017 | 2024-12-12 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 159dce23-b96f-38fd-a350-676a32e0a11a | -13.68774 | -54.76344 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28a2cdf1-4de1-330a-8a73-78f8d38ca1ce | -10.77646 | -52.07743 | 2024-12-12 04:40:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ab89824-beaf-3920-9906-e01e9b65c3f3 | -11.7815 | -55.13286 | 2024-12-12 04:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f401736-ca24-3e5a-9bec-ed0ed08cc06e | -11.20126 | -53.82244 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 629e8eeb-70d5-3516-aff1-cc58f19d25c5 | -11.20711 | -53.83213 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ea46b28-1be8-3f5d-aa4a-33ec4ccf8b91 | -11.11859 | -54.65301 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e8f8d33-0884-366b-8b6e-08281fa96aa8 | -13.17962 | -43.57402 | 2024-12-12 04:40:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b70113f8-1459-3fa7-b833-fa17de1382a0 | -13.69008 | -54.76194 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07f65462-0ac5-3830-a7c9-5337d59e72e1 | -11.11643 | -54.64289 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20b515b0-dcff-3032-bb34-bd6155bad26c | -12.49991 | -46.34744 | 2024-12-12 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7a9f43f-26a6-3e8c-8b52-f76f4dd97887 | -11.111 | -54.65163 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7114bbd0-d163-3b15-8a87-aa23caabc265 | -10.29273 | -53.69744 | 2024-12-12 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6731eb6-3cd8-3cd9-aede-1c0636d4a983 | -10.20125 | -36.21673 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 546c17ee-88a2-3f7e-9844-a91f985fd79d | -9.22772 | -47.81574 | 2024-12-12 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c41bbff-6276-3597-a80c-4029e91156b8 | -8.64321 | -46.0525 | 2024-12-12 04:40:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f361dea-cf65-3090-a76a-410e06bb9173 | -11.49186 | -48.19817 | 2024-12-12 04:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18e5a680-8e1c-3b86-9edc-db997197384a | -12.92346 | -55.04996 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b76f147e-65f1-395a-b25a-a86b2d58d0e1 | -11.11017 | -54.65636 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ed734f7-3794-3ee3-9d4b-b69e6997d32f | -11.20782 | -53.82789 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01cecb33-254e-3165-83d2-a60144ba5652 | -12.90362 | -48.59666 | 2024-12-12 04:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 724fdf1d-d693-393c-b902-b8a580e0935f | -11.68926 | -48.07752 | 2024-12-12 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0d77319-dcca-3132-bb96-f42c598121b7 | -10.29235 | -53.69625 | 2024-12-12 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b7328bb-cbf0-3493-badd-d7af624bcc12 | -11.68219 | -48.07646 | 2024-12-12 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4479bfd-bb88-3aca-ab21-d481c79098c7 | -13.37183 | -54.24611 | 2024-12-12 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a4bef06-9894-3a50-9e63-a9a805a7fe52 | -14.74342 | -52.6523 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c39d6501-5ca2-3742-8542-da7f5ddc082c | -11.19834 | -53.81759 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b801ee9c-63b0-3ffb-b204-c3033a50cfe9 | -11.44809 | -48.00595 | 2024-12-12 04:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 084e0788-0a1a-37f3-92e8-34311b1b2d16 | -10.19216 | -36.23093 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 0f44cbe1-06e1-3376-856d-e0e03c9f9d22 | -12.53784 | -57.73592 | 2024-12-12 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a85c5f01-0fd4-3ebc-8578-8513ef937255 | -13.68849 | -54.75902 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f3d3386-bcec-39ab-91a6-34423b5f581b | -13.693 | -54.76703 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5de6043b-1c40-3bfb-a214-1feb4bdca5fd | -11.47828 | -48.21334 | 2024-12-12 04:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f3c4e7d-ba6a-357a-936d-60ccbc307b6f | -12.65496 | -46.57781 | 2024-12-12 04:40:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19760178-4570-3c3e-9ab8-a66d9d4a0951 | -9.385 | -38.87956 | 2024-12-12 04:40:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8da06b5c-c729-3dd1-b71f-3558d22ecffe | -10.19373 | -36.22147 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 8ed14368-3252-30f3-aa20-e8433e0e433e | -13.32181 | -52.41381 | 2024-12-12 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1bbf570-82cf-34e4-8160-5084e800d994 | -10.19944 | -36.23174 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 4587dd16-44fe-3463-a805-1b25b3a462f2 | -11.68573 | -48.07699 | 2024-12-12 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cee2f84-ecdd-3f80-b5e8-7897c75f25a8 | -12.91886 | -55.05397 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cd5d415-1487-32f6-bfe8-407f4ad101e8 | -12.55138 | -58.34701 | 2024-12-12 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ae24546-f9a1-35f3-846b-875b88a23366 | -9.39174 | -38.87568 | 2024-12-12 04:40:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 685782eb-949f-3abc-99c6-3b4392a5338e | -11.11561 | -54.6476 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65bee186-dda9-360a-b5df-6e8fa991e31a | -14.74124 | -52.64437 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03e3bf4d-ea86-3cbf-8e0e-2e894f8fb1dd | -11.2049 | -53.82304 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68496c61-20ed-389a-87a7-10eba6d3214b | -9.19235 | -49.47706 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31c9125b-ff0c-353d-ac89-a0f217bfa645 | -14.74282 | -52.65598 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e321667-772e-3890-b3b6-55c9ee0100f6 | -9.60076 | -49.52323 | 2024-12-12 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0598f00c-c88c-3273-8dee-dc44b7d6f0d2 | -14.74064 | -52.64805 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c4a5170-e2b0-3baa-a017-d5e8685666dc | -11.19913 | -53.83516 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05379645-6836-3a20-945d-f075ba8c3498 | -9.23273 | -46.66695 | 2024-12-12 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41adb079-3ea5-3daf-80fb-ffa94320f723 | -9.343 | -47.83661 | 2024-12-12 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19a612ab-a780-3b4b-b95d-6c61eea1b65e | -13.06487 | -52.04209 | 2024-12-12 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 862f0f88-de86-3416-8cf8-7925fa652c95 | -11.84792 | -56.87052 | 2024-12-12 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4da2515a-cc50-357e-8f0d-eb424777ad27 | -11.2064 | -53.8364 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 878a21d1-902a-3633-b0cc-f1fcd936844c | -10.0017 | -47.5716 | 2024-12-12 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b63ae808-2657-35ad-b621-329113aaf758 | -11.20055 | -53.82668 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b65986b2-cc8f-3a4b-b762-1c4951c2abc1 | -12.92049 | -55.04459 | 2024-12-12 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e3d5ea5-bb7a-3e40-8d75-05e2726bc5ea | -11.11397 | -54.65705 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3efd28b0-3196-3db1-9e7e-9d771ac0e911 | -9.10981 | -49.46423 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d80ae055-36bc-3184-ab6a-91b17fc34b7d | -9.1126 | -49.46827 | 2024-12-12 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1e3793f-c7fc-32a3-8d24-97ae6908ceca | -11.20561 | -53.81881 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a601079-2b2f-38b2-9133-0c0f6e491429 | -13.26482 | -57.389 | 2024-12-12 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d183e916-026e-3ae7-b1e9-8ca71ac8e5cd | -13.37399 | -54.25525 | 2024-12-12 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da02c976-02a8-3993-a459-faec93de5ec1 | -13.07276 | -52.03597 | 2024-12-12 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 061a2f1d-a68c-37fa-b004-9bcbb02d85bf | -11.20197 | -53.8182 | 2024-12-12 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc8aa5a0-1f28-3213-b910-be31e26fdc77 | -8.6204 | -50.01748 | 2024-12-12 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa4c7f87-185c-31cf-b378-3c687e5d04b5 | -11.53656 | -51.27972 | 2024-12-12 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92534542-6e3b-346f-a354-ad3405610670 | -12.3294 | -49.99594 | 2024-12-12 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb34d54e-a841-3a1e-8267-437252e11fdc | -9.69731 | -36.18182 | 2024-12-12 04:40:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4ae9af30-f937-3459-9ba0-aeab5453772b | -10.20016 | -36.22981 | 2024-12-12 04:40:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| f627ecde-e492-38ba-b968-b51dbb3ed973 | -11.87327 | -43.71899 | 2024-12-12 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8d2b6c4-81af-3355-9177-ac3c6aa35ef4 | -14.74222 | -52.65964 | 2024-12-12 04:40:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9c0011b-6306-3ef1-bf6d-8b4c71869f20 | -8.39799 | -49.17549 | 2024-12-12 04:40:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README26.md)

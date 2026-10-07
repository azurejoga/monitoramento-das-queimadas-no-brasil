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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec3739f4-2646-3ee9-af97-410a84c2237f | -3.09561 | -54.15228 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f47645e-25d8-300a-beb3-f8c243e3a5d5 | -4.3053 | -50.78299 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5df9c117-41de-34d6-a5b8-5422af5de603 | -3.0506 | -54.26726 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2226462c-508c-3700-b056-39678078b854 | -3.10673 | -53.75485 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9f6b61d-be8a-3053-ae31-b8c9fc0f888a | -3.66911 | -60.62046 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4453f9fd-ffa9-3faf-a27c-a52319c7837f | -3.5105 | -51.67889 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e881a74-1697-34ba-a983-9b69f8ee79e4 | -3.50133 | -54.65088 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81626dd0-0ce6-3570-824d-94cdd667d288 | -3.10507 | -54.15734 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ffa82d4-0b85-3286-863b-7ecb1ce3068d | -4.15274 | -54.02802 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b0586b5-ec02-3cb2-8eaa-cf702daae2b5 | -2.7877 | -51.67907 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 59a40108-0184-3d6e-8625-3a7d9b516968 | -3.35947 | -50.47801 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e380879a-d5a5-3fa1-ad9f-dd19a0082c13 | -3.05935 | -54.14679 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b638746e-e88b-35c8-b09d-5e57a5e63a3d | -3.5068 | -51.67831 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2c035a6-31cd-315b-bee8-8ede63a0f001 | -3.34517 | -59.47702 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f09d6000-a3db-39e0-ae47-2e8c57ab9fa3 | -3.27716 | -54.01459 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f08ca634-3b79-3420-b1d6-b374d944f1b3 | -3.10956 | -53.78093 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e7640cb3-fd90-3916-a2d8-4d2eadc1961e | -2.40932 | -51.30377 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54137dee-f89c-318d-b204-98f47a1097b8 | -4.16066 | -55.15974 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53153cc5-e1a4-33b2-bfc2-1fe335e7b4c3 | -3.01324 | -54.13611 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9677580-1514-3b22-a23b-76a5a1858fd8 | -2.77624 | -54.10652 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 35c0f37d-9c69-3009-9daf-9ea02eb94caf | -3.05499 | -53.93304 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 703da818-4b36-39e6-a979-7388f60a3a8a | -1.88536 | -53.97223 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fbd2e82-93e0-3a84-9d55-47923c8bbc35 | -3.2772 | -54.03633 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ab367c93-d047-3c84-b67a-2319f5712c6e | -2.95838 | -54.15997 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12d44247-6e5c-3d77-9d5a-7a98606f03a4 | -3.28944 | -54.02371 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5333ac4f-8f90-3706-9550-9aa806751156 | -3.28669 | -54.04141 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d61fb881-2810-3e0c-96ea-114c98c8b0ae | -5.01246 | -50.93945 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1abb9d6-5901-32cf-abdb-8d60e582b9a2 | -6.14895 | -51.73373 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 660322be-bec5-35e4-8330-542105bafefd | -3.47829 | -59.47163 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a62164b4-bdc8-305d-85df-5a29ac0847ff | -3.92791 | -56.05999 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b07329af-da34-33ef-8c17-be4f62df5da8 | -3.5348 | -54.63464 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7a429cc7-20e2-3b9d-b18e-f3efcc33f8e1 | -3.68323 | -55.95065 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 845131af-04c7-3ecb-b882-aa9d8fdd272f | -2.04849 | -54.3003 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26ac3551-bf65-3939-93e7-4ca117f595fa | -3.02027 | -53.89134 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97e24b24-8a81-3b4a-89aa-e7cd36897e5a | -3.87447 | -55.81434 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c5f813e-7c20-36d3-b965-d9808da04f77 | -3.54812 | -59.49485 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daa9e32d-dd4d-3054-9b73-d03356d595f5 | -2.9861 | -54.77156 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68936594-30c7-35cc-855a-bfec5e4a6ac4 | -3.08709 | -54.25151 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e33cd0b6-ca65-34e3-a794-7cc02b6212b9 | -3.09886 | -53.73896 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f312e11c-bd3b-391e-81c0-b44a1c592907 | -6.73041 | -55.10591 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7163ec41-2827-3369-9bee-8d6310e1fbcf | -4.46624 | -54.9679 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac451462-6651-37e6-bb1f-f34523e4fa9c | -3.21903 | -54.30071 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a53c7d36-e1e9-3964-bb5c-98c097708a4f | -3.08617 | -54.30143 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27e27cc1-d610-3121-a943-39afb57ff99b | -6.21112 | -52.68601 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d119b97e-eddf-30c6-9a3e-95e065955bee | -3.66509 | -60.62011 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fece24d-f3c6-3ae2-ae9d-d39b35e1a9d4 | -3.08276 | -54.27946 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d795c2e-532d-3a69-8c77-bc50e45bd5b2 | -3.07128 | -54.17737 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 970c718b-59c3-329a-8e44-19f7970789fe | -5.99632 | -53.51163 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baa22e2c-c78d-3c06-b22b-62d4ffba9b2c | -4.15896 | -55.14893 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49f94899-a357-3f37-84ea-1fdb4095315a | -4.92463 | -55.86776 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96173496-45de-358a-b146-ba085045bd89 | -3.22568 | -54.30175 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd7f6858-587a-3e64-a7a6-af910bc8ba36 | -2.78337 | -51.68279 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0e6adad6-1a43-3ddb-8d98-2469280762e0 | -3.0983 | -54.28901 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0f87ae00-c036-3c22-8e9e-68fd6d8e816a | -4.77461 | -50.80819 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f53b9d-f3f7-3ae2-a303-106874f14ca0 | -3.11684 | -53.7784 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f22ab3e9-d050-3170-89f7-2eb021e7d56c | -3.04466 | -54.26274 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8eb5b09-b6ce-30a8-aa16-32e6f590bcdf | -3.21592 | -53.87783 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa5d7356-a0a1-3ae5-ac56-3de3eb3e312c | -4.11847 | -50.82359 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c6de984-7a8b-330c-91fe-68a00cc11fc2 | -3.05319 | -54.22839 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38a1b49c-b82c-3daf-8960-7552c6a3cfb5 | -2.97957 | -54.04448 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5251a346-ff39-306e-b369-e9985358d437 | -3.54163 | -50.09866 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bfb06ac9-f96c-3210-975d-b9e8efe7d491 | -4.14758 | -53.95013 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67e0c652-3b7b-3fef-8ce2-53ed23aa5e86 | -2.87947 | -54.07618 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 056f4550-bd96-3262-b317-1f64f9427e31 | -2.88063 | -54.09075 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46562dd9-17e2-32b3-a955-98738fcc694d | -2.97379 | -54.12637 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c6dcf4e-bd21-3174-b0f8-de41e2f6c5bf | -2.95518 | -54.13811 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34276eaa-6880-3e4d-97ab-a3cc4974ffe6 | -3.04209 | -53.90561 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fbceebd-9457-3298-b33a-91fd89047708 | -4.37879 | -59.90631 | 2026-10-07 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3081bd3e-4e7e-3a5f-a385-4ed9226b2331 | -2.93415 | -54.16362 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 333de601-9d3f-3787-b28a-9ddfd5ab974e | -2.96015 | -51.04199 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0131f294-dead-39cf-a0c5-7477270f284a | -3.22846 | -54.30577 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f58ed5d-306c-3915-b87d-78ba6bd2f35a | -3.53824 | -59.4124 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a1e9b41-9e0b-3871-bbd8-13763cc466bd | -3.71773 | -59.69197 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a5a50c7-bea9-329d-987f-a8eff2a3bf3d | -3.26992 | -54.0171 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cde0d80a-0f62-323e-9178-5782fb66226c | -3.63385 | -59.56457 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8593287d-f5df-389b-85cd-d394c43066bc | -3.5991 | -54.56996 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f287f792-bd30-3a1c-9908-3220b0beb867 | -3.80153 | -56.9968 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b2c35d-eefd-3dd0-8214-1acda81356b9 | -2.78404 | -51.67849 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7e35d1a3-cc13-3b66-a536-0e9282a7b087 | -3.27436 | -54.01053 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6144b55f-c560-3477-be84-580d5c97e349 | -4.92295 | -55.85693 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f23294ad-b334-3189-a013-d9c361751dff | -3.04774 | -53.93555 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ae190f7-7488-3ad0-9788-d5a896ee0101 | -3.50849 | -51.69204 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46635c5e-31be-37f5-bde3-26df2880a56a | -4.1595 | -55.14549 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 424d83c8-7393-321f-a94b-920750b99039 | -3.27819 | -54.18056 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fd780ee-528f-3c0c-ad8c-d1b24272a7ff | -3.07324 | -54.25294 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a19fb18-469d-336f-aa71-1b0ebbb09c6d | -1.95304 | -54.04031 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9237e370-963a-30d2-a4d1-5e35392757bb | -5.99979 | -53.51225 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ec8ce27-6216-367b-9b2e-291383a17bbc | -8.71678 | -45.18714 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 394cd6df-f22d-363d-9b08-53ca9343dd21 | -3.32434 | -54.19125 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9369163d-6135-3af5-9e03-4d5c6a9b5fe1 | -3.80974 | -47.4896 | 2026-10-07 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 91755371-7145-3e02-86bc-f6b5f02d0d74 | -3.9593 | -56.05425 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca88f31-9f31-3f20-878f-2f5ef253c5e4 | -3.16989 | -58.63276 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2130cb88-e039-326e-99a5-f50520dafb07 | -3.96603 | -56.12262 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16384742-7154-3832-b7cc-6eb145f3ed06 | -3.85637 | -55.99508 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83cd23f4-2579-3042-866e-d370e74d211a | -3.96261 | -56.05476 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb4d4708-4640-37b0-a5ce-3d583e95982e | -3.49016 | -54.6137 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f88390b-5d9a-3402-98a5-e053064a5db1 | -2.90962 | -54.12397 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc106e44-2f7f-3c27-95a0-2f87927345d2 | -4.26774 | -54.86574 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e15d64a-ffeb-3ac8-a402-59977716df4d | -2.56798 | -56.15989 | 2026-10-07 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7fcb10d-1056-3ffa-99d3-dfe811d96fc9 | -3.56334 | -59.49725 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README88.md)
